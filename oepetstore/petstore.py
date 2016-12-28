'''
This module for petstore
'''
# -*- coding: utf-8 -*-
from openerp import api, fields, models


class MessageOfTheDay(models.Model):
    '''
    This class create message of day
    '''
    _name = "oepetstore.message_of_the_day"

    @api.model
    def my_method(self):
        return {"hello": "world"}

    message = fields.Text()
    color = fields.Char(size=20)


class Product(models.Model):
    '''
    This class create module of Pet Toys List
    '''
    _inherit = "product.product"

    max_quantity = fields.Float(string="Maximum Quantity")
