# -*- coding: utf-8 -*-
{
    'name': "Order Lote",

    'summary': """ Order lot """,

    'description': """
        Order lot
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '1.03',

    'depends': ['stock','base','mrp'],
    
    'data': [
        'data/paperformat_ticket.xml',
        'security/ir.model.access.csv',
        #'views/stock_production_lot_views.xml',
        'views/mpr_order_production_lot.xml',
        #'views/mrp_bom.xml',
        'report/reporte_explosion_insumos.xml',
        'report/report.xml',
        #'report/reporte_codigo_barras_lote.xml',
        #'wizard/reporte_codigo_barras_lote_wizard.xml',
    ],
    'assets':{
        
    },
    'license': 'LGPL-3',
}
