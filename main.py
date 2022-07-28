from store import Store

class App:
    def __init__(self):
        self.productspath = 'data/products.json'
        self.cartpath = 'data/cart.json'
        self.discountpath = 'data/discount.json'
        self.products = []
        self.cart = []
        self.discounts = []
        self.FileLogging = False

    def getproductbyid(self):
        return Store.getproductbyid(self,1)

    def getproducts(self):
        return Store.getproducts(self)
    
    def addproduct(self):
        return Store.addproduct(self, "test", "test" , 20, 30)
    
    def removeproduct(self):
        return Store.removeproduct(self, 5)
    
    def getcart(self):
        return Store.getcart(self)
    
    def addtocart(self):
        return Store.addtocart(self,1,12, "KFDKSF")

    def removefromcart(self):
        return Store.removefromcart(self,1)

    def get_discounts(self):
        return Store.get_discounts(self )

    def add_discount(self):
        return Store.add_discount(self,"test",2,20,"kfdkskf")
    
    def removediscount(self):
        return Store.removediscounts(self, 5)

if __name__ == "__main__":
    app = App()
    app.getproducts()
    app.addproduct()
    app.removeproduct()
    app.getproductbyid()
    app.getcart()
    app.addtocart()
    app.removefromcart()
    app.get_discounts()
    app.add_discount()
    app.removediscount()
