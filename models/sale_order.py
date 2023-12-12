from odoo import models, fields, api
from datetime import datetime, timedelta


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    migrate = fields.Boolean(string='Migrated?')
    write_date_date = fields.Date(
        string='Write Date (Date Only)',
        compute='_compute_write_date_date',
        store=True,
    )

    @api.depends('write_date')
    def _compute_write_date_date(self):
        for record in self:
            # Extract the date part from write_date
            record.write_date_date = record.write_date.date()

    def rekap_sale_order(self):
        for record in self:
            self.env['so_sirkulasi.rekap_so'].create({
                'rekap_so_id': record.order_id.id,
                'product': record.product_template_id.name,
                'id_produk': record.product_template_id.id,
                'quantity': record.product_uom_qty,
                'transaction_date': record.write_date       
                })
            grouped_data = self.env['so_sirkulasi.rekap_so'].read_group(
                [('id_produk', '=', record.product_template_id.id),('transaction_date', '=', record.write_date_date)],
                ['id_produk', 'quantity:sum'],
                ['id_produk']
            )
            print(grouped_data, "ini grup data")
        
            total_quantity = grouped_data[0]['quantity'] if grouped_data else 0.0
            print(total_quantity, "ini total quantitiy")
            for total in record.order_id.env['so_sirkulasi.rekap_so'].search([('id_produk', '=', record.product_template_id.id)]):
                if total.transaction_date == record.write_date_date:
                    total.total_product = total_quantity

  
       







