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
    
 