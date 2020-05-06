# -*- encoding: utf-8 -*-
##############################################################################
#Copyright (c) 2015 - Present Teckzilla Software Solutions Pvt. Ltd. All Rights Reserved
#    Author: [Teckzilla Software Solutions]  <[sales@teckzilla.net]>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of the GNU General Public License is available at:
#    <http://www.gnu.org/licenses/gpl.html>.
#
##############################################################################

{
    "name" : "Base Shipping V11",
    "version" : "1.1.1",
    "depends" : ["base", "product","sale","stock","delivery","account"],
    "author" : "TeckZilla",
    "description": """
        Base Shipping V11\n
        Create Shipments\n
        Print Labels\n
    """,
    "website" : "www.teckzilla.net",
    'images': [],
    "category" : "Shipping",
    'summary': 'Base Shipping V11',
    "demo" : [],
	'currency': 'GBP',
    "data" : [

            'views/sequence.xml',
            'security/base_shipping_security.xml',
            'views/stock_picking_view.xml',
            'views/delivery_carrier.xml',
            'wizard/batch_force_availability.xml',
            'wizard/update_picking_view.xml',
            # 'wizard/print_picklist_view.xml',
            'wizard/search_pickings_view.xml',
            'views/base_carrier_code_view.xml',
            'views/manifest_view.xml',
            'report/base_manifest_report.xml',
            'report/base_manifest_template.xml',
            'views/report_paperformat.xml',
            'views/base_shipping_logs.xml',
            'views/product_view.xml',
            'wizard/res_config_settings.xml',
            'wizard/update_weight_dimension_wizard.xml',
            'security/ir.model.access.csv',


    ],
    'auto_install': False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


