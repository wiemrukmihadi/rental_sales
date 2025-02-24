# -*- coding: utf-8 -*-
{
    'name': "RentalSales",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/rental_order_view.xml',
        'views/rentalsales_product_view.xml',
        'views/rentalsales_sale_order_view.xml',
        'views/rentalsales_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

