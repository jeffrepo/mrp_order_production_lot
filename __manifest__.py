# -*- coding: utf-8 -*-
{
    'name': "Order Lote",

    'summary': """ Café Brujula """,

    'description': """
        Desarrollo para Café Brujula
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '1.01',

    'depends': ['stock','base','point_of_sale','hr_payroll','mrp','sale_stock','l10n_mx_edi_stock', 'pos_coupon','l10n_mx_edi','l10n_mx_edi_40','delivery','l10n_mx_edi_stock_30','l10n_mx_edi_stock_extended_31'],
    
    'data': [
        'data/paperformat_ticket.xml',
        'security/ir.model.access.csv',
        'views/stock_production_lot_views.xml',
        'views/mpr_order_production_lot.xml',
        'views/mrp_bom.xml',
        'report/report.xml',
        'report/reporte_codigo_barras_lote.xml',
        'wizard/reporte_codigo_barras_lote_wizard.xml',

        

    ],
    'qweb': [
        # 'static/src/xml/pos.xml',
    ],
    'assets':{
        
    },
    'license': 'LGPL-3',
}
