from odoo import models, fields, api, _


class res_partner(models.Model):
    _inherit = 'res.partner'

    ebay_user_id = fields.Char(string='UserID')


res_partner()
