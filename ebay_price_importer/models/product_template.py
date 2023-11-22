# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_ebay_price_importer(self):
        pricelist = self.env['product.pricelist'].search([], limit=1, order="sequence")

        for record in self:
            for item in pricelist.item_ids:
                if item.product_tmpl_id.id == record.id and item.compute_price == 'fixed':
                    record.write({'list_price': item.fixed_price})
                    break
