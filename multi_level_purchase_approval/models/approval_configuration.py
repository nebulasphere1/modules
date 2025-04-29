from odoo import models, fields, api

class ApprovalConfiguration(models.Model):
    _name = 'approval.configuration'
    _description = 'Approval Configuration'
    _rec_name = 'name'

    name = fields.Char(string="Approval Configuration",copy=False,require=1)
    minimum_amount = fields.Float(string="Minimum Amount")
    user_in_cc = fields.Boolean(string="User Always in CC")
    allowed_companies = fields.Many2many("res.company", string="Allowed Companies")

    approval_details = fields.One2many(comodel_name='purchase.approval.line',
                                       inverse_name='approval_id',
                                       string="Approval Details",
                                       )
    amount_on = fields.Selection([
        ('untaxed_amount', 'Untaxed Amount'),
        ('total', 'Total'),
    ], compute="_amount_on",
        readonly=True)
    total_level = fields.Integer(compute="_find_number_of_levels")

    def _find_number_of_levels(self):
        temp = 0
        for rec in self.approval_details:
            temp += 1
        self.total_level = temp

    def _amount_on(self):
        temp = self.env['ir.config_parameter'].sudo().get_param(
            'multi_user_dynamic_approval.amount_based_on')
        for rec in self:
            rec.amount_on = temp


