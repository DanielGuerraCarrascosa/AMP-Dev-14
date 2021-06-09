# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'sumary': """ Academy app para hacer pruebas""",
    
    'description': """ Modulo academia para realizar pruebas""",
    
    'author': 'Dani AMP Software',
    
    'Website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}