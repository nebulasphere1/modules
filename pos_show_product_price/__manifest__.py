# -*- coding: utf-8 -*-
{
    "name": "POS Product Price Display for Odoo 18 | Show Price Below Product in POS | Odoo POS Price Tag",
    "author": "NebulaSphere",
    "website": "https://www.nebulasphere.com",
    "support": "nebulasphere.team@gmail.com",
    "category": "Point of Sale",
    "summary": """
    Show product prices below product names in Odoo POS | POS price tag display | Enhance Odoo 18 POS UI for better visibility | Best product price display module for POS.
    """,
    "version": "18.0.1.0",
    "license": "OPL-1",
    "description": """
    🔥 Enhance your Odoo 18 POS experience with the **POS Product Price Display** module by NebulaSphere!

    This feature-rich addon enables **product price visibility directly below product names** in the POS interface, improving clarity and boosting sales efficiency. 

    🚀 Key Benefits:
    - Display product prices clearly below product images/names in POS.
    - Improve user experience for cashiers and customers.
    - Reduce billing errors and speed up sales.
    - Easy to configure via backend settings.
    - Fully compatible with Odoo 18.

    🛠️ Features:
    - Seamless integration with Odoo Point of Sale.
    - No technical expertise required.
    - Lightweight and performance-optimized.
    - Toggle price display on/off from settings.

    ✅ Perfect For:
    - Retail stores using Odoo POS
    - Supermarkets, Electronics shops, and Fashion outlets
    - Businesses with large product catalogs
    - Enterprises aiming for clear POS display for quicker checkouts

    🔎 SEO Keywords:
    - POS Product Price Display Odoo 18
    - Show Price Below Product Odoo POS
    - Display Product Price Odoo POS
    - Odoo 18 POS UI Customization
    - Product Price Visibility in Odoo POS
    - Best POS module for price display
    - Odoo POS enhancement modules
    - Odoo POS product pricing addon
    - POS Price Tag Display for Odoo
    - Custom POS product layout Odoo 18

    ✨ Upgrade your Odoo POS UI today with NebulaSphere’s price display module – the most efficient way to show product prices in your Point of Sale system.
    """,
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_show_product_price/static/src/app/**/*",
        ],
    },
    "installable": True,
    "auto_install": False,
    "application": True,
    "images": ["static/description/banner.png"],
    "price": 25,
    "currency": "USD",
}
