from cart import Cart
from discount import Discount
from product import Product

class App:
    import logging
    logging.basicConfig(filename='debug.log',
                    format='{timestamp : 1658994433495, "message": "{ "functioncalled": "%(funcName)s()" , "output": "%(message)s" }"]},',
                    level=logging.DEBUG)
    def __init__(self):
        self.productspath = 'data/products.json'
        self.cartpath = 'data/cart.json'
        self.discountpath = 'data/discount.json'
        self.products = []
        self.cart = []
        self.discounts = []
        
    def load_products(self):
        return Product.getproducts(self)
    
    def load_cart(self):
        return Cart.getcart(self)

    def load_discount(self):
        return Discount.get_discounts(self)

if __name__ == "__main__":
    app = App()
    app.load_products()
    # app.load_cart()
    # app.load_discount()