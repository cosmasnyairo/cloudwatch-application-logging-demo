
from collections import OrderedDict

import json
import logging
import os

from utility.utility import deletefromfile, readfromfile, writetofile

class Discount:
    def __init__(self, productid, name, discountpercentage, discountcode):
        self.name = name
        self.productid = productid
        self.discountpercentage = discountpercentage
        self.discountcode = discountcode

    def to_ordered_dict(self):
        return OrderedDict([
            ('name', self.name),
            ('productid', self.productid),
            ('discountpercentage', self.discountpercentage),
            ('discountcode', self.discountcode)
        ])

    def __repr__(self):
        return str(self.__dict__)

    def get_discounts(self):
        if os.path.exists(self.discountpath):
            with open(self.discountpath) as json_file:
                self.discounts = [ x.__dict__ for x in [Discount(
                    discount['name'],
                    discount['productid'],
                    discount['discountpercentage'],
                    discount['discountcode'],
                ) for discount in json.load(json_file)]]
        return(self.discounts)

    def add_discount(self, name, productid, discountpercentage, discountcode):
        data = {}
        discount = []
        data["name"] = name
        data["productid"] = productid
        data["discountpercentage"] = discountpercentage
        data["discountcode"] = discountcode
        discount = readfromfile(self, self.discountpath, discount)
        writetofile(self, self.discountpath, discount, data)

    def removediscounts(self, productid):
        discount = []
        discount = readfromfile(self, self.discountpath, discount)
        deletefromfile(self, self.discountpath, discount, productid)
