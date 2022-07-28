import os
from datetime import date
import json
import os
from cart import Cart
from discount import Discount
from product import Product
from utility.utility import deletefromfile, logtoFile, readfromfile, sendlogstocloudwatch, writetofile

class Store:
    def __init__(self) :
        self.productspath = 'data/products.json'
        self.cartpath = 'data/cart.json'
        self.discountpath = 'data/discount.json'
        self.products = []
        self.cart = []
        self.discounts = []
        self.FileLogging = True

    def getproductbyid(self, productid):
        self.getproducts()
        if self.FileLogging:
            logtoFile('INFO', productid)
        else:
            sendlogstocloudwatch('INFO', productid,
                                 "Product with id: %s was fetched" % productid)
        return [x for x in self.products if x['productid'] == productid][0]

    def getproducts(self):
        if os.path.exists(self.productspath):
            with open(self.productspath) as json_file:
                self.products = [x.__dict__ for x in [Product(
                    product['productid'],
                    product['name'],
                    product['description'],
                    product['price'],
                    product['stockquantity'],
                ) for product in json.load(json_file)]]
        if self.FileLogging:
            logtoFile('INFO', self.products)
        else:
            sendlogstocloudwatch('INFO', self.products,
                                 "products were fetched")
        return self.products

    def addproduct(self, description, name, price, stockquantity):
        data = {}
        products = []
        data["description"] = description
        data["name"] = name
        data["price"] = price
        data["stockquantity"] = stockquantity
        products = readfromfile(self.productspath, products)
        data["productid"] = len(products)+1
        writetofile(self.productspath, products, data)
        if self.FileLogging:
            logtoFile('INFO', data)
        else:
            sendlogstocloudwatch('INFO', data, "A product was added")

    def removeproduct(self, productid):
        products = []
        products = readfromfile(self.productspath, products)
        deletefromfile(self.productspath, products, productid)
        if self.FileLogging:
            logtoFile('WARNING', productid)
        else:
            sendlogstocloudwatch('WARNING', productid,
                                 " The product id %s was removed" % productid)

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
        if self.FileLogging:
              logtoFile( 'INFO', self.cart)
        else: sendlogstocloudwatch('INFO', self.cart, "items from cart were fetched")
        return(self.cart)

    def addtocart(self, productid, quantity, discountcodes):
        added = self.getproductbyid()
        data = {}
        cart = []
        data["productid"] = productid
        data["quantity"] = quantity
        data['totalprice'] = added['price'] * data['quantity']
        data["discountcodes"] = discountcodes
        data["date"] = date.today().strftime("%B %d, %Y")
        cart = readfromfile(self.cartpath, cart)
        writetofile(self.cartpath, cart, data)
        if self.FileLogging:
              logtoFile( 'INFO', data)
        else: sendlogstocloudwatch('INFO', data, "items were added to cart")

    def removefromcart(self,productid):
        cart = []
        cart = readfromfile(self.cartpath, cart)
        deletefromfile( self.cartpath, cart, productid)
        if self.FileLogging:
              logtoFile( 'WARNING', productid)
        else: sendlogstocloudwatch('WARNING', productid, " Product id %s was removed from cart" % productid)
    
    
    def get_discounts(self):
        if os.path.exists(self.discountpath):
            with open(self.discountpath) as json_file:
                self.discounts = [x.__dict__ for x in [Discount(
                    discount['name'],
                    discount['productid'],
                    discount['discountpercentage'],
                    discount['discountcode'],
                ) for discount in json.load(json_file)]]
        if self.FileLogging:
            logtoFile( 'INFO', self.discounts)
        else:
            sendlogstocloudwatch('INFO', self.discounts, "Discounts were fetched")
        return(self.discounts)

    def add_discount(self, name, productid, discountpercentage, discountcode):
        data = {}
        discount = []
        data["name"] = name
        data["productid"] = productid
        data["discountpercentage"] = discountpercentage
        data["discountcode"] = discountcode
        discount = readfromfile(self.discountpath, discount)
        writetofile(self.discountpath, discount, data)
        if self.FileLogging:
              logtoFile('INFO', data)
        else: sendlogstocloudwatch('INFO', data, "Discount code was added")

    def removediscounts(self, productid):
        discount = []
        discount = readfromfile(self.discountpath, discount)
        deletefromfile(self.discountpath, discount, productid)
        if self.FileLogging:
              logtoFile('WARNING', productid)
        else: sendlogstocloudwatch('WARNING', productid, " A discount code for %s was removed" % productid)