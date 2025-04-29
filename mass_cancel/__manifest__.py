# -*- coding: utf-8 -*-
# © 2024 NebulaSphere
# Email: nebulasphere.team@gmail.com

{
    'name': 'Mass Cancel Orders (Sales, Purchases, Invoices) | Bulk Cancel Orders | Cancel Button',
    'author': 'NebulaSphere',
    'website': 'https://www.nebulasphere.com',
    'support': 'nebulasphere.team@gmail.com',
    'category': 'Sales, Purchase, Accounting',
    'version': '17.0.1.0',
    'price': 12,
    'currency': 'USD',
    'summary': 'NebulaSphere App - Cancel multiple Sales Orders, Purchase Orders, and Invoices at once. Bulk Cancel in Odoo 18.',
    'description': """
NebulaSphere - Mass Cancel Orders for Odoo
===========================================
Cancel multiple Sales Orders, Purchase Orders, and Customer/Supplier Invoices at once with a single click.

Key Features:
--------------
✔ Mass cancel Sales Orders  
✔ Mass cancel Purchase Orders  
✔ Mass cancel Invoices (Customer & Vendor Bills)  
✔ Simple and user-friendly UI  
✔ Permission-based access control  
✔ Fully compatible with Odoo 18

SEO Keywords:
---------------
NebulaSphere Mass Cancel Orders Odoo, Bulk Cancel Sales Purchase Invoice Odoo, Cancel Multiple Orders Odoo, Odoo 17 Mass Cancel, Batch Cancel Orders Odoo, Mass Cancel Button NebulaSphere,
 Sales Order Cancel Odoo, Purchase Order Cancel Odoo, Invoice Cancel Odoo, Odoo Apps Bulk Cancel.

Why choose our app?
--------------------
- Are you tired of canceling records one by one?
- Want to save time in your business process?
- Need a secure and easy way to cancel multiple documents?
- Looking for a solution to cancel orders in bulk in Odoo?

Our Mass Cancel module by NebulaSphere is your answer!

License:
----------
This app is licensed under the Odoo Proprietary License (OPL-1).

""",
    'license': 'OPL-1',
    'depends': ['base', 'sale_management', 'purchase', 'account'],
    'data': [
        'security/groups.xml',
        'views/mass_cancel_action.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
