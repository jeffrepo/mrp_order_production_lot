from re import findall as regex_findall
from re import split as regex_split

from odoo.tools.misc import attrgetter
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    elaboration_date = fields.Date('Fecha de elaboración')
