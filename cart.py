from collections import OrderedDict

import json
import logging
import os

from utility.utility import deletefromfile, readfromfile, writetofile
                    
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
    
    def getcart(self):
        if os.path.exists(self.cartpath):
            with open(self.cartpath) as json_file:
                self.cart = [ x.__dict__ for x in [Cart(
                    cartitem['productid'],
                    cartitem['quantity'],
                    cartitem['totalprice'],
                    cartitem['discountcodes'],
                    cartitem['date'],
                ) for cartitem in json.load(json_file)]]
        logging.debug(str(self.cart))
        return(self.cart)

    def addtocart(self, productid, quantity, totalprice, discountcodes,date):
        added = self.getproductbyid(productid)
        data = {}
        cart = []
        data["productid"] = productid
        data["quantity"] = quantity
        data['totalprice'] = totalprice
        data["discountcodes"] = discountcodes
        data["date"] =  date
        # date.today().strftime("%B %d, %Y")
        cart = readfromfile(self, self.cartpath, cart)
        writetofile(self, self.cartpath, cart, data)

    def removefromcart(self,productid):
        cart = []
        cart = readfromfile(self, self.cartpath, cart)
        deletefromfile(self, self.cartpath, cart, productid)