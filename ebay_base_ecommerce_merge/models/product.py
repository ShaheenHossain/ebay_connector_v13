from odoo import api, fields, models, _


def get_allocation():
    return True


class product_product(models.Model):
    _inherit = 'product.product'

    @api.model
    def copy(self, id, default=None):
        if not default:
            default = {}
        default.update({
            'default_code': False,
            'images_ids': False,
        })
        return super(product_product, self).copy(id, default)

    def get_main_image(self, id):
        if isinstance(id, list):
            id = id[0]
        images_ids = self.read(id, ['image_ids'])['image_ids']
        if images_ids:
            return images_ids[0]
        return False

    #    def _get_main_image(self, cr, uid, ids, field_name, arg, context=None):
    #        res = {}
    #        img_obj = self.pool.get('product.images')
    #        for id in ids:
    #            image_id = self.get_main_image(cr, uid, id, context=context)
    #            if image_id:
    #                image = img_obj.browse(cr, uid, image_id, context=context)
    #                res[id] = image.file
    #            else:
    #                res[id] = False
    #        return res

    def _get_main_image(self):
        img_obj = self.env['product.images']
        for id in self:
            image_id = self.get_main_image(id)
            if image_id:
                #                image = img_obj.browse(cr, uid, image_id, context=context)
                # image = image_id
                id.product_image = image_id.file
            else:
                id.product_image = False

    image_ids = fields.One2many('product.images', 'product_id', string='Product Images')
    default_code = fields.Char(string='SKU', size=64, require='True')

    #    product_image = fields.Binary(compute='_get_main_image',  method=True)
    allocation_history_id = fields.One2many('product.allocation.history', 'alloc_history_id',
                                            string='Allocation History', readonly=True)


class product_allocation_history(models.Model):
    _name = 'product.allocation.history'

    date = fields.Datetime(string='Date of Allocation', readonly=True)
    name = fields.Many2one('sale.shop', string='Shop', readonly=True)
    alloc_history_id = fields.Many2one('product.product', string='Product')
    qty_allocate = fields.Float(string='Allocated Quantity', readonly=True)


