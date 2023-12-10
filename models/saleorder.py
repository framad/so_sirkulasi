from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sirkulasi_ok = fields.Boolean('Sirkulasi Product')
    rekap_so_ids = fields.One2many(comodel_name="so_sirkulasi.rekap_so", inverse_name='rekap_so_id')

    