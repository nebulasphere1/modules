# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_price = fields.Boolean(
        string='Show Price in POS',
        related='pos_config_id.is_price',
        readonly=False
    )
    pos_config_id = fields.Many2one(
        'pos.config',
        string="POS Configuration",
        required=True,
        default=lambda self: self.env['pos.config'].search([], limit=1).id
    )

    def set_values(self):
        super().set_values()
        if self.pos_config_id:
            self.pos_config_id.is_price = self.is_price