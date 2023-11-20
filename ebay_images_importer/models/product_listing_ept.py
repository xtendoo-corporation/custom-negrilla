# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
"""
Describes eBay product listings
"""
import logging
from odoo import models, fields, api, _


class EbayProductListingEpt(models.Model):
    """
    Describes eBay Product Listing fields and methods.
    """
    _inherit = "ebay.product.listing.ept"


    @api.model_create_multi
    def create(self, vals_list):
        res = super(EbayProductListingEpt, self).create(vals_list)
        for vals in vals_list:
            print("*"*80)
            print("vals en create", vals)
            print("res en create", res)
            print("*"*80)

        return res

    def write(self, vals):
        res = super(EbayProductListingEpt, self).write(vals)
        for record in self:
            print("*"*80)
            print("record en write", record)
            print("*"*80)
        return res


class EbayProductListingEpt(models.Model):
    _inherit = "ebay.product.listing.ept"


    def create_or_update_product_images(self, picture_urls, ebay_product):
        res = super(EbayProductListingEpt, self).create_or_update_product_images(picture_urls, ebay_product)

        print('*' * 80)
        print('picture_urls', picture_urls)
        print('ebay_product', ebay_product)
        print('res', res)
        print('*' * 80)

        return res

