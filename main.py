import json
from turtle import pen
from urllib import response
from store import Store

from flask import Flask, jsonify, request

store = Store()
app = Flask(__name__)


@app.route('/getproduct', methods=['POST'])
def getproductid():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    productid = values['productid']
    product = store.getproductbyid(productid)
    return jsonify(product), 200


@app.route('/getproducts', methods=['GET'])
def getproducts():
    products = store.getproducts()
    return jsonify(products), 200


@app.route('/addproduct', methods=['POST'])
def addproduct():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    description, name, price, stockquantity = values['description'], values[
        'name'], values['price'], values['stockquantity']
    addedproduct = store.addproduct(description, name, price, stockquantity)
    return jsonify(addedproduct), 200


@app.route('/removeproduct', methods=['DELETE'])
def removeproduct():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    productid = values['productid']
    store.removeproduct(productid)
    response = {
        'message': 'Product removed successfully!',
        'removedproductid': productid
    }
    return jsonify(response), 200


@app.route('/getcart', methods=['GET'])
def getcart():
    cart = store.getcart()
    return jsonify(cart), 200


@app.route('/addtocart', methods=['POST'])
def addtocart():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    productid, quantity, discountcodes = values['productid'], values['quantity'], values['discountcodes']
    cartitem = store.addtocart(productid, quantity, discountcodes)
    return jsonify(cartitem), 200


@app.route('/removefromcart', methods=['DELETE'])
def removefromcart():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    productid = values['productid']
    store.removefromcart(productid)
    response = {
        'message': 'Product removed from cart successfully!',
        'removedproductid': productid
    }
    return jsonify(response), 200


@app.route('/getdiscounts', methods=['GET'])
def get_discounts():
    discount = store.get_discounts()
    return jsonify(discount), 200


@app.route('/adddiscount', methods=['POST'])
def add_discount():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    name, productid, discountpercentage, discountcode = values['name'], values[
        'productid'], values['discountpercentage'], values['discountcode']
    discountcode = store.add_discount(
        name, productid, discountpercentage, discountcode)
    return jsonify(discountcode), 200


@app.route('/removediscount', methods=['DELETE'])
def removediscount():
    values = request.get_json()
    if not values:
        response = {'message': 'No data found!'}
        return jsonify(response), 400
    productid = values['productid']
    store.removediscounts(productid)
    response = {
        'message': 'Discount removed successfully!',
        'productid associated': productid
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run()
