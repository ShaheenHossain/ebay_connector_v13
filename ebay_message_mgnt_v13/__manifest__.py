{
    "name": "Ebay Messaging",
    "version": "1.1.1",
    "depends": ['ebay_odoo_v13'],
    "author": "Planet-Odoo",
    "description": """
       Messaging management:
       1) get Messages from ebay
       2) Reply to those messages
    """,
    "website": "www.planet-odoo.com",
    'images': [],
    "category": "ecommerce",
    'summary': 'Ebay integration',
    "demo": [],
    "data": [
        'wizard/compose_message_view.xml',
        'views/sale_view.xml',
        'views/ebay_messages_view.xml',
        # 'views/ebay_msg_data.xml'
    ],
    'auto_install': False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


