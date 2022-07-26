
from collections import OrderedDict


class Discount:
    def __init__(self, productid, name, discount, discountcode, datevalid):
        self.name = name
        self.productid = productid
        self.discount = discount
        self.discountcode = discountcode
        self.datevalid = datevalid

    def to_ordered_dict(self):
        return OrderedDict([
            ('name', self.name),
            ('productid', self.productid),
            ('discount', self.discount),
            ('discountcode', self.discountcode),
            ('datevalid', self.datevalid)
        ])

    def __repr__(self):
        return str(self.__dict__)
