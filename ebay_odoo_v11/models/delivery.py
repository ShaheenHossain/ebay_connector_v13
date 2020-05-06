import time
import odoo.addons.decimal_precision as dp
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class delivery_carrier(models.Model):
    _inherit = "delivery.carrier"

    carrier_code = fields.Char(tring='Carrier Code', size=150)
    ship_type = fields.Selection([('standard', 'Standard'), ('expedited', 'Expedited')], string='Shipping Service Type',
                                 default='standard')


delivery_carrier()


class res_partner(models.Model):
    _inherit = "res.partner"

    ebay_user_id = fields.Char(string='Ebay Customer ID', size=256)


res_partner()
