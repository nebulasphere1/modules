from odoo import models, fields, api

class PurchaseApprovalLine(models.Model):
    _name = 'purchase.approval.line'
    _description = 'Purchase Approval Line'

    approve_process_by = fields.Selection([
        ('user', 'User'),
        ('group', 'Group'),
    ],string="Approve Process By",default="user",required=1)

    level = fields.Integer(string="level")
    user_id = fields.Many2many("res.users")
    process_approved_by = fields.Many2one("res.users")
    group_id = fields.Many2many("res.groups")

    approval_id = fields.Many2one('approval.configuration', string="Purchase approval order")

    purchase_order_id= fields.Many2one('purchase.order', string="Purchase order")

    status = fields.Boolean(string="Status")
    approved_date = fields.Date(string="Approved Date")
    purchase_order = fields.Char(string="Purchase Order")
