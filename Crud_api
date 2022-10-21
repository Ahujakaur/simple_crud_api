#import functions
from urllib import response
from flask import Flask, jsonify, request
from unicodedata import name
from bson import json_util
import pymongo
from pymongo import MongoClient


myclient= pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["my database"]
mycol=mydb['products']

app = Flask(__name__)


#assign route
@app.route('/home') 
def home():  
    return jsonify({ "welcome"}) 

#Testing process to see if it works or not
@app.route('/products')
def getProducts():
    product={
        "name":"name",
        "price":"price",
        "quantity":"quantity"    }
    db=myclient.myproduct
    return jsonify({"done"})

@app.route('/<string:product_name>')
def getProduct(product_name):
    dblist=myclient.list_database_nmae()
    print("database exists")
    
        


@app.route('/addproducts', methods=['POST'])
#insert
def mydb():
    _json=request.json
    _name=_json['name']
    _price=_json['price']
    _quantity=_json['quantity']
    x=mycol.insert_one(mydb)
    print(x.insert_ids)
    return jsonify({"updated successfully"})

@app.route('/products/name', methods=['PUT'])
def editProduct(product_name):
    x=mycol.insert_one(mydb)
    print(x)
    return jsonify({"updated successfully"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    # list comprehension
    #productFound = [product for product in myproduct if product['name'] == product_name]
    myquery={" name": "name", "price":"price","quantity":"quantity"}
    mycol.delete_one(myquery)
        
    return jsonify({"message": "Product Not Found"})

    

if __name__ == '__main__':
    app.run(debug=True, port=4000)
