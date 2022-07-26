
import json
import os
from re import A
from cart import Cart
from discount import Discount
from order import Order

from product import Product


class App:
    def __init__(self):
        self.productspath = 'data/products.json'
        self.cartpath = 'data/cart.json'
        self.discountpath = 'data/discount.json'
        self.orderspath = 'data/order.json'

        self.get_products()
        self.get_cart()
        self.get_discounts()
        self.get_orders()

    def get_products(self):
        if os.path.exists(self.productspath):
            with open(self.productspath) as json_file:
                products = [Product(
                    product['id'],
                    product['name'],
                    product['description'],
                    product['rating'],
                    product['price'],
                    product['stockquantity'],
                ) for product in json.load(json_file)]
                return(products, "\n")

    def get_cart(self):
        if os.path.exists(self.cartpath):
            with open(self.cartpath) as json_file:
                cart = [Cart(
                    cartitem['productid'],
                    cartitem['quantity'],
                    cartitem['totalprice'],
                    cartitem['discountcodes'],
                    cartitem['date'],
                ) for cartitem in json.load(json_file)]
                return(cart, "\n")

    def get_discounts(self):
        if os.path.exists(self.discountpath):
            with open(self.discountpath) as json_file:
                discounts = [Discount(
                    discount['name'],
                    discount['productid'],
                    discount['discount'],
                    discount['discountcode'],
                    discount['datevalid'],
                ) for discount in json.load(json_file)]
                return(discounts, "\n")

    def get_orders(self):
        if os.path.exists(self.orderspath):
            with open(self.orderspath) as json_file:
                orders = [Order(
                    order['orderid'],
                    order['totalprice'],
                    order['productids'],
                    order['discountcodes'],
                    order['date'],
                ) for order in json.load(json_file)]
                print(orders, "\n")

if __name__ == "__main__":
    app = App()
