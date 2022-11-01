from odoo import fields,models

class FirstModel(models.Model):
    _name = "aldim.first"
    _description = "AldiM Training First Model"

    nama = fields.Char(
        string= "Nama Mahasiswa",
        required= True,
        index= True,
        help= 'Nama Mahasiswa Sesuai PDDikti'
    )
    nim = fields.Char(
        string='NIM',
        required=True,
        index=True,
        help='NIM Mahasiswa sesuai Pddikti'
    )
    jenis_kelamin = fields.Selection(
        string='Jenis Kelamin',
        selection=[('pria', 'Pria'), ('wanita', 'Wanita')],
        help="Jenis Kelamin Mahasiswa"
    )
    univ = fields.Char(
        string= "Nama Universitas",
        required= True,
        index= False,
        help= 'Asal Universitas Sesuai PDDikti'
    )
    semester = fields.Integer(
        string='Semester Saat Ini',
        required=True,
        help='Semester Mahasiswa sesuai Pddikti'
    )
    asal = fields.Char(
        string= "Alamat Tempat Tinggal",
        required= True,
        index= False,
        help= 'Alamat Tempat Tinggal Sesuai KTP'
    )
    kos = fields.Char(
        string= "Alamat Kos",
        required= True,
        index= False,
        help= 'Asal Kos Saat Ini'
    )
    ipk = fields.Float(
        string= "IPK saat ini",
        required= True,
        help= 'IPK mahasiswa saat ini'
    )
    
