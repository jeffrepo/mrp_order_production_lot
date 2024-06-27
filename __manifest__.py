# -*- coding: utf-8 -*-
{
    'name': "Order Lote",

    'summary': """ Desarrollo extra quemen """,

    'description': """
        Desarrollo extra pra quemen
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '1.01',

    'depends': ['stock','base','point_of_sale','hr_payroll','mrp','sale_stock','l10n_mx_edi_stock', 'pos_coupon','l10n_mx_edi','l10n_mx_edi_40','delivery'],

    'data': [
        'security/ir.model.access.csv',
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
