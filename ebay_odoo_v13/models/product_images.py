from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import base64, urllib
import datetime
# import cStringIO
# import StringIO
from io import StringIO
# from urllib import urlencode
from urllib.parse import urlencode
# import Image
import os
from base64 import b64decode


class product_images(models.Model):
    _inherit = "product.images"

    is_ebay = fields.Boolean(string='Ebay Image')