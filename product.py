
from collections import OrderedDict
import json
import os

from utility.utility import deletefromfile, readfromfile, writetofile, logtoFile, sendlogstocloudwatch


class Product:
    def __init__(self, productid, name, description, price, stockquantity):
        self.productid = productid
        self.name = name
        self.description = description
        self.price = price
        self.stockquantity = stockquantity

    def to_ordered_dict(self):
        return OrderedDict([
            ("name", self.name),
            ("productid", self.productid),
            ("description", self.description),
            ("price", self.price),
            ("stockquantity", self.stockquantity)
        ])

    def __repr__(self):
        return str(self.__dict__)
