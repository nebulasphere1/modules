# -*- coding: utf-8 -*-
from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    is_price = fields.Boolean(string='Show Price in POS', default=False)

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        if 'pos.config' not in res:
            res.append('pos.config')
        return res

    def _get_pos_ui_pos_config(self, params):
        return self.search_read(
            [('id', '=', self.env.context.get('pos_config_id'))],
            ['is_price'],
        )