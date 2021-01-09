# See LICENSE file for full copyright and licensing details.

{
    'name': 'IDC',
    #'version': '14.0.1.',
    'author': 'Global Business Home S.L.',
    'website': 'http://www.gbh-business.com',
    'category': 'Course Center Management',
    'complexity': 'easy',
    'Summary': 'A Module For Courses Management',
    'images': ['static/description/IDC.jpg'],
    'depends': ['hr', 'crm'],
    'data': ['security/school_security.xml',
             'security/ir.model.access.csv',
             'views/student_view.xml',
             'views/school_view.xml',
             'views/teacher_view.xml',
             'views/parent_view.xml',
             'views/report_view.xml',
             'views/identity_card.xml',
             'views/template_view.xml'],
    'installable': True,
    'application': True
}
