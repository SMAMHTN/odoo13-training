from odoo import fields,models

class FirstModel(models.Model):
    _name = "aldim.first"
    _description = "AldiM Training First Model"

    boolean_test = fields.Boolean(
        string='Boolean',
        required=True,
        index=False,
        help='Testing boolean'
    )
    char_test = fields.Char
    int_test = fields.Integer
    float_test = fields.Float
    selection_type = fields.Selection(
        string='Selection',
        selection=[('choice1', 'Choice1'), ('choice2', 'Choice2')],
        help="This is for testing choice")
    
