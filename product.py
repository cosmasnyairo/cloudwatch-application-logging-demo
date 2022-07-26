
from collections import OrderedDict


class Product:
    def __init__(self, productid, name, description, rating, price, stockquantity):
        self.productid = productid
        self.name = name
        self.description = description
        self.rating = rating
        self.price = price
        self.stockquantity = stockquantity

    def to_ordered_dict(self):
        return OrderedDict([
            ('productid', self.id),
            ('name', self.name),
            ('description', self.description),
            ('rating', self.rating),
            ('price', self.price),
            ('stockquantity', self.stockquantity)
        ])

    def __repr__(self):
        return str(self.__dict__)
