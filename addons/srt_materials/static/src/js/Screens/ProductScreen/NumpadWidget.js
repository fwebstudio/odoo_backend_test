odoo.define('srt_materials.NumpadWidget', function (require) {
    'use strict';

//    var screens = require('point_of_sale.screens');
//
//    screens.NumpadWidget.include({
//
//        renderElement: function(){
//            this._super();
//            this.$el.find('.mode-button[data-mode="discount"]').prop('disabled', true);
//        }
//
//    });


    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    class NumpadWidget extends PosComponent {
        mounted() {
            // IMPROVEMENT: This listener shouldn't be here because in core point_of_sale
            // there is no way of changing the cashier. Only when pos_hr is installed
            // that this listener makes sense.
            this.hasPriceControlRights = false;
            this.hasManualDiscount = false;
            this.env.pos.on('change:cashier', () => {
                if (!this.hasPriceControlRights && this.props.activeMode === 'price') {
                    this.trigger('set-numpad-mode', { mode: 'quantity' });
                }
            });
        }
        willUnmount() {
            this.env.pos.on('change:cashier', null, this);
        }
        get hasPriceControlRights() {
            const cashier = this.env.pos.get('cashier') || this.env.pos.get_cashier();
            return !this.env.pos.config.restrict_price_control || cashier.role == 'manager';
        }
        get hasManualDiscount() {
            return this.env.pos.config.manual_discount;
        }
        changeMode(mode) {
            if (!this.hasPriceControlRights && mode === 'price') {
                return;
            }
            if (!this.hasManualDiscount && mode === 'discount') {
                return;
            }
            this.trigger('set-numpad-mode', { mode });
        }
        sendInput(key) {
            this.trigger('numpad-click-input', { key });
        }
        get decimalSeparator() {
            return this.env._t.database.parameters.decimal_point;
        }
    }
    NumpadWidget.template = 'NumpadWidget';

    Registries.Component.add(NumpadWidget);

    return NumpadWidget;
});