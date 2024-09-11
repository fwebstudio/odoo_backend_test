# -*- coding: utf-8 -*-
{
    'name': "Materials For Test",

    'summary': """
        This modules is for testing purpose only""",

    'description': """
        Testing purpose for Altech Omega Andalan
    """,

    'author': "Gee Kresnadi",
    'website': "http://www.kresnadi.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'point_of_sale'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/res_material_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            # 'srt_materials/static/src/js/Screens/ProductScreen/NumpadWidget.js',
            'srt_materials/static/src/xml/pos_templates.xml',
        ],
    },
}
