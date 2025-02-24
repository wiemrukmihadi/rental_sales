# -*- coding: utf-8 -*-

from odoo import _, models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_rent  = fields.Boolean(string='Can be rented')
    count_rent  = fields.Integer(compute="_compute_count_rent")

    @api.depends('is_rent')
    def _compute_count_rent(self):
        rent_count = self.env['product.template'].search_count([('is_rent', '=', True)])
        for record in self:
            record.count_rent = rent_count

    def action_rental_products(self):
        return {
            "name": _("Rental Product"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "product.template",
            "target": "current",
            "domain": [("is_rent", "=", True)],
            "context": {"default_is_rent": self.id}
        }

