{
    'name' : 'AldiM Custom Module',
    'version': '1.2',
    'category': 'AldiM/AldiM',
    'summary': 'Modul Custom AldiM',
    'depends': ['base','sale'],
    'description': """
Modul Custom AldiM.
===============================================

Modul Custom.
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/aldim.first.csv',
        'views/aldim_first_views.xml',
        # 'views/aldim_first_menu.xml'
        # 'views/aldim_ext_sales_view.xml',
        # 'report/aldim_ext_sales_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}