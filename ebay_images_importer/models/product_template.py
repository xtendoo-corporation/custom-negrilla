# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_ebay_product_syncro(self):
        ebay_product_template_ept = self.env['ebay.product.template.ept']
        pricelist = self.env['product.pricelist'].search([], limit=1, order="sequence")

        for record in self:
            if len(record.ept_image_ids) > 1:
                for image in record.ept_image_ids[1:]:
                    image_vals = {
                        "name": image.url,
                        "image_1920": image.image,
                        "product_tmpl_id": record.id,
                    }
                    if len(self.env["product.image"].search([("name", "=", image.url)])) == 0:
                        self.env["product.image"].create(image_vals)

            if not record.image_1920 and record.ept_image_ids:
                record.image_1920 = record.ept_image_ids[0].image

            ebay_product_template_ept_ids = ebay_product_template_ept.search(
                [("product_tmpl_id", "=", record.id)],
            )
            for ebay_product_template_ept in ebay_product_template_ept_ids:
                record.description_sale = tools.html2plaintext(ebay_product_template_ept.description)

            for item in pricelist.item_ids:
                if item.product_tmpl_id.id == record.id and item.compute_price == 'fixed':
                    record.list_price = item.fixed_price
                    break

