7/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ComboConfiguratorPopup } from "@point_of_sale/app/store/combo_configurator_popup/combo_configurator_popup";

patch(ComboConfiguratorPopup.prototype, {
    /**
     * Override the formattedComboPrice method.
     * @param {Object} comboItem - The combo item object.
     * @returns {String} - The formatted price string.
     */
    formattedComboPrice(comboItem) {
        const extra_price = comboItem.extra_price;
        const product = comboItem.product_id;

        // Get the base price of the product
        const base_price = product.lst_price; // Assuming lst_price is the base price

        if (this.env.utils.floatIsZero(extra_price)) {
            // If extra_price is zero, return only the base price
            return this.env.utils.formatCurrency(base_price);
        } else {
            // Calculate the total price (base_price + extra_price)
            const total_price = this.pos.getProductPrice(product, extra_price);

            // Format both base_price and total_price
            const formatted_base_price = this.env.utils.formatCurrency(base_price);
            const formatted_total_price = this.env.utils.formatCurrency(total_price);

            // Return a string that includes both base_price and total_price
            return `Base Price: ${formatted_base_price}, Total Price: ${formatted_total_price}`;
        }
    },
});