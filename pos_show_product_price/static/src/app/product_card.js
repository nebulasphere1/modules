/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { useService } from "@web/core/utils/hooks";

patch(ProductCard.prototype, {
    setup() {
        super.setup();
        this.pos = useService("pos");
    },

    get config() {
        return this.pos.config || {};
    },

    get price() {
        const product = this.props.product;
        if (!product) {
            console.warn("Product is undefined in ProductCard");
            return "N/A";
        }
        // Use lst_price directly or fallback to getProductPrice
        const price = product.lst_price || this.pos.getProductPrice(product, 0);
        if (!price || price === 0) {
            console.warn(`Price for product ${product.display_name} is 0 or undefined`);
            return "0.00";
        }
        return this.env.utils.formatCurrency(price);
    },
});