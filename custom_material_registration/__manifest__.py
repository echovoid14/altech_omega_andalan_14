# -*- coding: utf-8 -*-
{
    'name': "Custom Material Registration",
    'summary': """
        Module to manage material registration including supplier and pricing information.
    """,
    'description': """
        This module allows users to register and manage materials, including details such as material types, pricing, and supplier information.
    """,
    'author': "Michael Hubert",
    'website': "http://www.yourcompany.com",
    
    'category': 'Inventory/Materials',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_registration.xml', 
        'menu_item.xml'
    ],
    'installable': True,
    'auto_install': False,
}
