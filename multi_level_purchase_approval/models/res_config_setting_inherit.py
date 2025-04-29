from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    amount_based_on = fields.Selection([
        ('untaxed_amount', 'Untaxed Amount'),
        ('total', 'Total'),
    ],config_parameter='multi_user_dynamic_approval.amount_based_on')