
from collections import OrderedDict

import json
import logging
import os

from utility.utility import deletefromfile, readfromfile, writetofile

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

    def getproductbyid(self, productid):
        self.getproducts()
        return [x for x in self.products if x.productid == productid][0]

    def getproducts(self):
        if os.path.exists(self.productspath):
            with open(self.productspath) as json_file:
                self.products = [ x.__dict__ for x in[Product(
                    product['productid'],
                    product['name'],
                    product['description'],
                    product['price'],
                    product['stockquantity'],
                ) for product in json.load(json_file)]]   
        return self.products

    def addproduct(self, description, name, price, stockquantity):
        data = {}
        products = []
        data["description"] = description
        data["name"] = name
        data["price"] = price
        data["stockquantity"] = stockquantity
        products = readfromfile(self,  self.productspath, products)
        data["productid"] = len(products)+1
        writetofile(self, self.productspath, products, data)

    def removeproduct(self,productid):
        products = []
        products = readfromfile(self, self.productspath, products)
        deletefromfile(self, self.productspath, products, productid)