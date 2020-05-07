from odoo import api, fields, models, _

import odoo.netsvc


class stock_picking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"

    shop_id = fields.Many2one('sale.shop', string='Shop')