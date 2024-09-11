# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SrtPointOfSale(models.Model):
    _inherit = 'pos.order'
    _description = 'Inherited Point Of Sales'
