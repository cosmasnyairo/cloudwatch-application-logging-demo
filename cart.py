from collections import OrderedDict
from datetime import date

import json
import os

from utility.utility import deletefromfile, logtoFile, readfromfile, sendlogstocloudwatch, writetofile

from product import Product     

class Cart:
    def __init__(self, productid, quantity, totalprice, discountcode, date):
        self.productid = productid
        self.quantity = quantity
        self.totalprice = totalprice
        self.discountcode = discountcode
        self.date = date

    def to_ordered_dict(self):
        return OrderedDict([
            ('productid', self.productid),
            ('quantity', self.quantity),
            ('totalprice', self.totalprice),
            ('discountcode', self.discountcode),
            ('date', self.date)
        ])

    def __repr__(self):
        return str(self.__dict__)
    
    # def getcart(self):
    #     if os.path.exists(self.cartpath):
    #         with open(self.cartpath) as json_file:
    #             self.cart = [ x.__dict__ for x in [Cart(
    #                 cartitem['productid'],
    #                 cartitem['quantity'],
    #                 cartitem['totalprice'],
    #                 cartitem['discountcodes'],
    #                 cartitem['date'],
    #             ) for cartitem in json.load(json_file)]]
    #     if self.FileLogging:
    #           logtoFile( 'INFO', self.cart)
    #     else: sendlogstocloudwatch('INFO', self.cart, "items from cart were fetched")
    #     return(self.cart)

    # def addtocart(self, productid, quantity, discountcodes):
    #     added = Product.getproductbyid(productid)
    #     data = {}
    #     cart = []
    #     data["productid"] = productid
    #     data["quantity"] = quantity
    #     data['totalprice'] = added['price'] * data['quantity']
    #     data["discountcodes"] = discountcodes
    #     data["date"] = date.today().strftime("%B %d, %Y")
    #     cart = readfromfile(self, self.cartpath, cart)
    #     writetofile(self, self.cartpath, cart, data)
    #     if self.FileLogging:
    #           logtoFile( 'INFO', data, "items were added to cart")
    #     else: sendlogstocloudwatch('INFO', data, "items were added to cart")

    # def removefromcart(self,productid):
    #     cart = []
    #     cart = readfromfile(self, self.cartpath, cart)
    #     deletefromfile(self, self.cartpath, cart, productid)
    #     if self.FileLogging:
    #           logtoFile( 'WARNING', productid, " Product id %s was removed from cart" % productid)
    #     else: sendlogstocloudwatch('WARNING', productid, " Product id %s was removed from cart" % productid)
       