from odoo import api, fields, models, _


class product_attribute_value(models.Model):
    _inherit = "product.attribute.value"

    value = fields.Char(string='Label', size=100)
    imported = fields.Boolean(string='Imported', default=False)


product_attribute_value()


class product_attribute(models.Model):
    _inherit = "product.attribute"

    def get_leaf(self):
        res = True
        for rec in self:
            attrs_ids = self.search([('parent_id', '=', rec.id)])
            if not attrs_ids:
                rec.write({'is_leaf': True})
        return res

    attribute_code = fields.Char(string='Attribute Code', size=255)
    attr_set_id = fields.Many2one('product.attribute.set', string='Attribute Set')
    parent_id = fields.Many2one('product.attribute', string='Parent', default=False)
    pattern = fields.Selection([('choice', 'Choice'),
                                ('restricted', 'Ristricted'),
                                ('other', 'Other')], string='Product Type Pattern')

    is_leaf = fields.Boolean(string="Leaf", default=False)
    imported = fields.Boolean(string="Imported")


product_attribute()


class product_attribute_set(models.Model):
    _name = "product.attribute.set"

    name = fields.Char(string='Name', size=255)
    code = fields.Char(string='Code', size=255)
    imported = fields.Boolean(string='Import')
    shop_id = fields.Many2one('sale.shop', string='Shop')
    attribute_ids = fields.One2many('product.attribute', 'attr_set_id', string='Attributes')


class product_attribute_info(models.Model):
    _name = "product.attribute.info"

    name = fields.Many2one('product.attribute', string='Attribute', required=True)
    value = fields.Many2one('product.attribute.value', string='Values')
    value_text = fields.Text(string='Text')