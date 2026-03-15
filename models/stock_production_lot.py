# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'

    elaboration_date = fields.Date('Fecha de elaboración')
