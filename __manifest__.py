{
    'name': 'Disciplinary Actions',
    'version': '18.0.1.0.0',
    'author': 'Yohannes Shiwerekey',
    'category': 'Human Resources',
    'summary': 'Manage employee disciplinary cases with decision-based tracking',
    'description': """
        Track and manage employee disciplinary cases. Features include:
        - Decision-based disciplinary actions (Verbal, Written, Last)
        - Discipline Analytical Reports (Pivot, Graph)
        - Employee profile integration with decision counters and kanban badges.
    """,
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
