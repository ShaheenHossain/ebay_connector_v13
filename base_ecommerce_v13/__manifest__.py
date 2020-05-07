{
    "name": "Base Ecommerce v13",
    "version": "1.1",
    "depends": ['base', 'sale', 'product', 'stock', 'sale_stock', 'delivery', "account", 'base_shipping_v13'],
    "author": "Planet Odoo",
    "description": """
    Base Module for All MarketPlaces Management\n
    """,
    "website" : "www.planet-odoo.com",
    'images': [],
    "category": "ecommerce",
    'summary': 'Base Module For All E-Commerce Modules',
    "demo": [],
    "data": [
            'security/base_ecommerce_security.xml',
            'security/ir.model.access.csv',
#            'report/sale_report_custom_view.xml',
            'view/instance_view.xml',
            'view/sale_view.xml',
            'view/payment_view.xml',
            'view/log_view.xml',
            'view/import_sequence.xml',
            'view/attribute_view.xml',
            'view/base_menu_view.xml',
            'view/product_images_view.xml',
            'view/attribute_view.xml',
            'wizard/update_marketplace_price_view.xml',
            'wizard/update_bulk_carrier_view.xml',
#            'wizard/test_view.xml',
            'view/product_view.xml',
            'view/res_partner_view.xml',
            'view/logger_view.xml',
#            'payment.method.ecommerce.csv'
    ],
    'auto_install': False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

