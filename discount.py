
from collections import OrderedDict

import json
import os

from utility.utility import deletefromfile, logtoFile, readfromfile, sendlogstocloudwatch, writetofile


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

   