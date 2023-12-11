# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ebay_product_template_ept_id = fields.Many2one(
        comodel_name='ebay.product.template.ept',
        string='Ebay Product Template',
        ondelete='cascade',
        copy=False,
    )

    def action_ebay_images_importer(self):
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

            print("*"*80)
            print(record.ebay_product_template_ept_id.description)
            print("*"*80)

            if record.ebay_product_template_ept_id.description:
                record.description_sale = record.ebay_product_template_ept_id.description
