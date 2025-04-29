from datetime import date

from odoo import models, fields, api

class PurchaseOrderReject(models.TransientModel):
    _name = 'purchase.order.reject.wizard'
    _description = 'Purchase Order Reject Wizard'

    purchase_id = fields.Many2one('purchase.order', string='Sale Order')
    reason = fields.Html(string="Reason")

    @api.model
    def default_get(self, fields):
        res = super(PurchaseOrderReject, self).default_get(fields)
        res['purchase_id'] = self.env.context.get('default_purchase_id')
        return res

    def reject_purchase_order(self):
        self.purchase_id.reject_date = date.today()
        self.purchase_id.reject_by =  self.env.user
        self.purchase_id.reject_reason = self.reason
        self.purchase_id.state = 'reject'
        self.purchase_id.next_approval_level = None
        self.purchase_id.users = None
        self.purchase_id.groups = None
        self.purchase_id.users.env['bus.bus']._sendone(
            self.purchase_id.partner_id,
            "simple_notification",
            {
                'title': "Notification",
                'message': f"Dear User!! your purchase order {self.purchase_id.name} is rejected",
                'sticky': True,
                'type': 'danger'
            }
        )

        template = self.env.ref('multi_user_dynamic_approval.email_template_order_reject')
        email_values = {'email_to': self.purchase_id.approval_created_by.email}
        template.send_mail(self.purchase_id.id, force_send=True, email_values=email_values)
