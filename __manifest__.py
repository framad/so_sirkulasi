# -*- coding: utf-8 -*-
{
    'name': "SO Sirkulasi",

    'summary': """
        SO Sirkulasi""",

    'description': """
       SO Sirkulasi
    """,

    'author': "Febry",
    'website': "framad.github.io/framadhan",

    'category': 'Uncategorized',
    'version': '0.1',

		# Dependency
    'depends': ['base','sale'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/menuteims.views.xml',
        'views/sales_order_clone.views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}