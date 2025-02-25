# -*- coding: utf-8 -*-

from odoo import _, models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_rent  = fields.Boolean(string='Can be rented')
    count_rent  = fields.Integer(compute="_compute_count_rent")

    @api.depends('is_rent')
    def _compute_count_rent(self):
        for record in self:
            record.count_rent = self.env['sale.order.line'].search_count([
                ('product_template_id', '=', record.id),
                ('order_id.rental_status', '=', 'reserved')
            ])

    def action_view_reserved_orders(self):
        """Show Sale Orders where this product is rented and in Reserved status"""
        sale_orders = self.env['sale.order.line'].search([
            ('product_id.product_tmpl_id', '=', self.id),
            ('order_id.rental_status', '=', 'reserved')
        ]).mapped('order_id')

        return {
            'name': 'Reserved Sale Orders',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'domain': [('id', 'in', sale_orders.ids)],
            'views': [(self.env.ref('rental_sales.view_sale_order_reserved_tree').id, 'tree'),
                  (False, 'form')],
            'context': {'default_rental_status': 'reserved'},
        }

