from odoo import api, fields, models, SUPERUSER_ID, _
from datetime import date
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
import logging
import pytz


class QuemenOpLoteLinea(models.Model):
    _name = "mrp_order_production_lot.op_lote_line"
    _rec_name = "product_id"

    lot_id = fields.Many2one("mrp_order_production_lot.op_lote", "Lote")
    product_id = fields.Many2one('product.product','Producto',tracking=True)
    quantity = fields.Float('Cantidad',tracking=True)
    elaboration_date = fields.Date('Fecha elaboracion',tracking=True)
    qty_label = fields.Float('Cantidad etiquetas', default=1)
    lot_barcode_id = fields.Many2one('stock.production.lot', 'Lote',tracking=True)
    lot_state = fields.Selection(
        [('borrador', 'Borrador'), ('confirmado', 'Confirmado')],
        'Estado', readonly=True, copy=False, related='lot_id.state')    
    # wizard_id = fields.Many2one('quemen.reporte_codigo_barras.wizard', 'Wizard')

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.product_id:
            self.qty_label = self.quantity
