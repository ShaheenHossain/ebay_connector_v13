from odoo import models, fields, api, _


class update_marketplace_price(models.TransientModel):
    _name = 'update.marketplace.price'

    name = fields.Char(string='Name', size=64)
    shop_id = fields.Many2one('sale.shop', string='Shop')

    def update_price(self):
        return True

    def update_stock(self):
        return True

    def update_stock_price(self):
        return True
