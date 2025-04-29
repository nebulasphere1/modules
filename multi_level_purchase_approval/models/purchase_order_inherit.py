from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    approval_level = fields.Many2one("approval.configuration", string="Approval Level", copy=False,
                                     compute="_find_approval_level", store=True)
    state = fields.Selection(selection_add=[
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To approve'),
        ('waiting for approval', 'Waiting for Approval'),
        ('reject', 'Reject'),
        ('purchase', 'Purchase Order'),
        ('done', 'Lock'),
        ('cancel', 'Cancelled'),
    ])
    next_approval_level = fields.Integer(string="Next Approval Level", readonly=True, copy=False)
    users = fields.Many2many("res.users", string="Users", readonly=True, copy=False)
    groups = fields.Many2many("res.groups", string="Groups", readonly=True, copy=False)

    reject_date = fields.Date(string="Reject Date", readonly=True, copy=False)
    reject_by = fields.Many2one("res.users", string="Reject By", readonly=True, copy=False)
    reject_reason = fields.Html(string="Reject Reason", readonly=True, copy=False)
    order_approve_by = fields.Many2one("res.users", string="Order Approve By", readonly=True, copy=False)
    approval_created_by = fields.Many2one("res.users", string="Approval Created By", readonly=True, copy=False)


    purchase_approval_line_details = fields.One2many(
        comodel_name='purchase.approval.line',
        inverse_name='purchase_order_id',
        string="Level Details",
        copy=False
    )
    is_current_approver = fields.Boolean(compute='_is_current_approver')

    def _is_current_approver(self):
        temp = False
        for rec in self.users:
            if self.env.user.partner_id == rec.partner_id:
                temp = True
        self.is_current_approver = temp

    @api.depends('order_line.price_unit', 'order_line.product_qty')
    def _find_approval_level(self):
        approval_config = self.env['approval.configuration'].search([])
        temp_list = []
        for rec in approval_config:
            if rec.amount_on == 'untaxed_amount':
                if self.amount_untaxed > rec.minimum_amount:
                    temp_list.append(rec)
            elif rec.amount_on == 'total':
                if self.amount_total > rec.minimum_amount:
                    temp_list.append(rec)
        temp = 0
        if len(temp_list) > 0:
            temp = temp_list[0]

        for i in range(1, len(temp_list)):
            if temp_list[i].minimum_amount > temp.minimum_amount:
                temp = temp_list[i]

        if temp and temp != 0:
            self.approval_level = temp
        print(temp)

    def button_confirm(self):
        if self.approval_level:
                if self.approval_level.total_level <= 0:
                    return super(PurchaseOrderInherit, self).button_confirm()
                else:
                    self.purchase_approval_line_details.unlink()
                    sorted_approval_details = sorted(
                        self.approval_level.approval_details,
                        key=lambda x: x.level
                    )
                    print(sorted_approval_details)
                    for rec in sorted_approval_details:
                        self.env['purchase.approval.line'].create({
                            'purchase_order_id': self.id,
                            'user_id': rec.user_id.ids,
                            'group_id': rec.group_id.ids,
                            'level': rec.level,
                            'status': rec.status,
                        })

                    self.state = 'waiting for approval'
                    self.next_approval_level = min(rec.level for rec in sorted_approval_details)
                    self.reject_reason = None
                    self.reject_by = None
                    self.reject_date = None
                    self.approval_created_by = self.env.user

                    self._assign_users_and_notify()
        else:
            return super(PurchaseOrderInherit,self).button_confirm()

    curr_level = fields.Integer(default=1, copy=False)

    def approve_order(self):
        current_line = next(
            (line for line in self.purchase_approval_line_details if line.level == self.next_approval_level),
            None
        )

        if self.env.user.partner_id not in self.users.partner_id:
            raise ValidationError("You are not the authorized approver for the current level.")

        current_line.status = True
        current_line.approved_date = date.today()
        current_line.process_approved_by = self.env.user
        self.order_approve_by = self.env.user

        sorted_levels = sorted(
            line.level for line in self.purchase_approval_line_details
        )
        print(sorted_levels)
        if self.next_approval_level == sorted_levels[-1]:
            self.state = 'purchase'
            self.next_approval_level = None
            self.users = None
            self.groups = None
            template = self.env.ref('multi_user_dynamic_approval.email_template_order_confirm')
            email_values = {'email_to': self.approval_created_by.email}
            template.send_mail(self.id, force_send=True,email_values=email_values)
            return super(PurchaseOrderInherit,self).button_confirm()

        else:
            next_index = sorted_levels.index(self.next_approval_level) + 1
            self.next_approval_level = sorted_levels[next_index]
            self._assign_users_and_notify()

    def _assign_users_and_notify(self):
        curent_line = next(
            (line for line in self.purchase_approval_line_details if line.level == self.next_approval_level), None
        )
        if curent_line:
            self.users = curent_line.user_id
            self.groups = curent_line.group_id
            self.users = curent_line.group_id.users if curent_line.group_id else curent_line.user_id

            template = self.env.ref('multi_user_dynamic_approval.email_template_purchase_approval')
            for user in self.users:

                if self.order_approve_by:
                    email_values = {'email_to': user.email, 'email_from': self.order_approve_by.email}
                    template.send_mail(self.id,force_send=True, email_values=email_values)
                else:
                    email_values = {'email_to': user.email}
                    template.send_mail(self.id,force_send=True, email_values=email_values)
                user.env['bus.bus']._sendone(
                    user.partner_id,
                    "simple_notification",
                    {
                        'title': "Notification",
                        'message': f"You have an approval notification for purchase order {self.name}",
                        'sticky': True,
                        'type': 'info'
                    }
                )

    def reject_order(self):
        if self.env.user.partner_id in self.users.partner_id:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Purchase Order Reject',
                'res_model': 'purchase.order.reject.wizard',
                'target': 'new',
                'view_mode': 'form',
                'context': {
                    'default_purchase_id': self.id
                },
            }
        else:
            raise ValidationError("You are not the authorize approver for the current level.")

    def button_draft(self):
        self.curr_level = 1
        return super(PurchaseOrderInherit, self).button_draft()

