{
    'name': 'Disciplinary Actions',
    'version': '18.0.1.0.0',
    'author': 'Top Technologies',
    'category': 'Human Resources',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/disciplinary_sequence.xml',
        'views/disciplinary_action_views.xml',
        'views/hr_employee_inherit.xml',
        'views/disciplinary_action_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
