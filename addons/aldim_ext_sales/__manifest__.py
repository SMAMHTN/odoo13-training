{
    'name' : 'Sales Extended AldiM',
    'version': '1.1',
    'category': 'Sales/Sales',
    'depends': ['base','sale'],
    'description': """
Modul Sales AldiM.
===============================================

Modul sales dengan adanya tambahan end_user sebagai tujuan akhir
penerima barang.
    """,
    'data': [
        'views/aldim_ext_sales_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}