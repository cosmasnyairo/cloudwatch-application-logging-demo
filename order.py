
from collections import OrderedDict
from pickle import LIST



class Order:
    def __init__(self, orderid, totalprice, productids, discountcodes, date):
        self.orderid = orderid
        self.totalprice = totalprice
        self.productids = productids
        self.discountcodes= discountcodes
        self.date = date

    def to_ordered_dict(self):
        return OrderedDict([
            ('orderid', self.orderid),
            ('totalprice', self.totalprice),
            ("productids", self.productids),
            ('discountcodes', self.discountcodes),
            ('date', self.date)
        ])

    def __repr__(self):
        return str(self.__dict__)
