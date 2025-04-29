{
    'name': 'Multi-Level Purchase Approval',
    'version': '18.0',
    'category': 'Purchase',
    'depends': ['base', 'purchase', 'mail'],
    'author': 'nebulasphere',
    'license': 'OPL-1',
    'support': 'nebulasphere.team@gmail.com',
    'maintainer': 'nebulasphere',
    'summary': 'Streamline purchase order approvals with dynamic, multi-level workflows in Odoo 18.',
    'description': """
Dynamic Purchase Approval for Odoo 18
====================================

Enhance your Odoo purchase management with flexible, multi-level approval workflows. This module allows you to configure dynamic approval rules based on purchase order amounts (total or untaxed), assign approvers (users or groups), and automate notifications for seamless procurement processes.

**Key Features:**
- **Dynamic Approval Rules**: Set minimum amounts for approvals, configurable by company.
- **Multi-Level Approvals**: Define multiple approval levels with specific users or groups.
- **Flexible Amount Basis**: Choose between total or untaxed amount for approval thresholds.
- **Automated Notifications**: Send email alerts for approvals, confirmations, and rejections.
- **User-Friendly Interface**: Approve or reject orders directly from the purchase order form.
- **Rejection Workflow**: Record rejection reasons via a wizard for transparency.
- **Settings Integration**: Configure approval settings in the Purchase module.

**Use Cases:**
- Automate approval workflows for large purchase orders.
- Ensure compliance with internal procurement policies.
- Improve transparency with detailed approval tracking.

**Why Choose This Module?**
- Fully compatible with Odoo 18.
- Easy to configure and integrate with existing purchase processes.
- Boosts efficiency by reducing manual approval delays.

**Installation:**
1. Install the module via the Odoo Apps menu.
2. Configure approval rules in Settings > Purchase.
3. Set up approval levels and assign approvers.
4. Create purchase orders and trigger the approval workflow.

**Support:**
For assistance, contact us at nebulasphere.team@gmail.com.

**Keywords:**
purchase approval, dynamic approval, multi-level approval, purchase workflow, Odoo purchase, procurement, purchase order management, approval automation, Odoo 18 purchase, purchase compliance, purchase process optimization

**Screenshots:**
- Approval Configuration Form
- Purchase Order Approval View
- Settings for Amount Basis
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/approval_configuration_view.xml',
        'views/purchase_approval_line_view.xml',
        'views/purchase_order_inherit_view.xml',
        'views/res_config_settings_view.xml',
        'wizard/purchase_order_reject.xml',
        'demo/mail_templates.xml',
    ],
    'demo': [],
     "images": [
        "static/description/banner.png",
        "static/description/icon.png",
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

    'price': 35.00,
    'currency': 'USD',
}