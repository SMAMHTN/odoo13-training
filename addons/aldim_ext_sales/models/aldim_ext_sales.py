from odoo import fields,models

class aldim_ext_sales_model(models.Model):
    _inherit='sale.order'
    _description="Perpanjangan form sales"
    _order = 'date_order desc, id desc'

    end_user = fields.Many2one(
        'res.partner',
        string='End User',
        required=True,
        index=False,
        help='User Akhir yang akan menerima pesanan( Dropship)'
    )