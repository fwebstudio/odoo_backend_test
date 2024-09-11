# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SrtResMaterial(models.Model):
    _name = 'res.material'
    _description = 'Resource Material'

    code = fields.Char(string='Material Code', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    name = fields.Char("Material Name", required=True)
    type = fields.Selection(selection=[('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')],
                            string="Material Type", required=True)
    price = fields.Float(string="Material Buy Price", help="Price higher than 100")
    supplier = fields.Many2one(comodel_name='res.partner', string="Related Supplier")

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('res.material') or _('New')
        result = super(SrtResMaterial, self).create(vals)
        return result

    @api.constrains('price')
    def _check_price(self):
        for material in self:
            print(material.price)
            if material.price < 100:
                raise ValidationError(
                    _('You cannot have a price below 100 (price written: %s)',
                      material.price))

