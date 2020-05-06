/* 
    OpenERP, Open Source Management Solution
    This module copyright (C) 2014 Therp BV (<http://therp.nl>)
                          (C) 2013 Marcel van der Boom <marcel@hsdev.com>
    Copyright (C) 2016 Serpent Consulting Services Pvt. Ltd.
                            (<http://www.serpentcs.com>)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

odoo.define('web_tree_image.WebTreeImage', function (require) {
    "use strict";
    var core = require('web.core');
    var session = require('web.session');
    var QWeb = core.qweb;
    var list_widget_registry = core.list_widget_registry;
    var registry = require('web.field_registry');
    var FieldManagerMixin = require('web.FieldManagerMixin');
    var Widget = require('web.Widget');
    var ListView = require('web.ListView');




    var WebTreeImage = registry.get('image').extend({
    _render: function () {
            /* Return a valid img tag. For image fields, test if the
             field's value contains just the binary size and retrieve
            the image from the dedicated controller in that case.
            Otherwise, assume a character field containing either a
            stock Odoo icon name without path or extension or a fully
            fledged location or data url */
            var self = this;
            var url = this.placeholder;

			self.session = session
//
            if (!this.res_id || !this.value) {
                return '';
            }

            var value = this.value, src;
            if (this.formatType === 'binary') {

                if (value && value.substr(0, 10).indexOf(' ') === -1) {
                    // The media subtype (png) seems to be arbitrary
                    src = "data:image/png;base64," + value;

                } else {
                    var imageArgs = {
                        model: this.model,
                        field: this.nodeOptions.preview_image || this.name,
                        id: this.res_id
                    }
                    if (this.resize) {
                        imageArgs.resize = this.resize;
                    }
                    src = self.session.url('/web/binary/image', imageArgs);

                }

            } else {
//                if (!/\//.test(row_data[this.id].value)) {
                if(1==1) {
                    src = '/web/static/src/img/icons/' + this.name + '.png';

                } else {
                    src = this.res_id.value;
                }
            }



            this.height=this.attrs.height;
            this.width=this.attrs.width;
            var $img = QWeb.render('ListView.row.image', {widget: this, src: src});
            this.$('> img').remove();
            this.$el.prepend($img);
        }
    });

    registry
    .add('image_resize', WebTreeImage)
    console.log("----f--hh--%s",registry.get('image_resize'));

});





