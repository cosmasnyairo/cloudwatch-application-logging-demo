import json
import boto3
import time
from cart import Cart
from discount import Discount
from product import Product


class Upload():
    def __init__(self):
        self.productspath = 'data/products.json'
        self.cartpath = 'data/cart.json'
        self.discountpath = 'data/discount.json'
        self.products = []
        self.cart = []
        self.discounts = []
        self.client = boto3.client('logs', region_name="eu-west-1")
        self.seq_token = None
        self.loggroup = 'test'
        self.logstream = 'test6'
    
    def sequenceToken(self):
        logdescribe = self.client.describe_log_streams(logGroupName=self.loggroup, logStreamNamePrefix=self.logstream)
        logStreams = logdescribe['logStreams']
        logStream = logStreams[0]
        sequenceToken = logStream['uploadSequenceToken']
        self.seq_token = sequenceToken


    def sendlogstocloudwatch(self, function, loglevel):
        logmessage = {
            "loglevel ": loglevel,
            "functioncalled": "%s()"%(function.__name__),
            "output" : function(self)
        }
        self.sequenceToken()
        log_event = {
                'logGroupName': self.loggroup,
                'logStreamName': self.logstream,
                'logEvents': [
                    {
                        'timestamp': int(round(time.time() * 1000)),
                        'message': json.dumps(logmessage),
                    },
                ],
                'sequenceToken' : self.seq_token
        }
        self.client.put_log_events(**log_event)
        print("Logs for %s() function call sent successfully"%(function.__name__))

if __name__ == "__main__":
    app = Upload()
    app.sendlogstocloudwatch(Product.getproducts, "DEBUG")
    app.sendlogstocloudwatch(Cart.getcart, "DEBUG")
    app.sendlogstocloudwatch(Discount.get_discounts, "DEBUG")
    
    
    