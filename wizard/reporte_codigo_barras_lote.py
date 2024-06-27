# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _

class ReporteCodigoBarrasWizard(models.TransientModel):
    _name = 'mrp_order_production_lot.reporte_codigo_barras_wizard'
    _description = 'Reporte de Códigos de Barras'

    def _domain_product_ids(self):
        domain = []
        id = self.env.context.get('active_ids', [])
        op_lot_id = self.env['mrp_order_production_lot.op_lote'].search([('id', '=', id)])
        if op_lot_id:
            domain = [('id', 'in', op_lot_id.product_ids.ids)]
        return domain

    product_ids = fields.Many2many(
        'mrp_order_production_lot.op_lote_line',
        string='Productos',
        relation='op_lote_line_reporte_wizard_rel', 
        column1='wizard_id',
        column2='product_id',
        domain=_domain_product_ids
    )

    def print_report(self):
        data = {
            'ids': [],
            'model': 'mrp_order_production_lot.reporte_codigo_barras_wizard',
            'form': self.read()[0],
        }

        product_ids = data['form']['product_ids']
        data['product_ids'] = product_ids

        report_reference = self.env.ref('mrp_order_production_lot.action_report_codigo_barras_lote').report_action(self, data=data)
        report_reference.update({'close_on_report_download': True})
        return report_reference
