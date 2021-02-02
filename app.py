from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route("/pin")
def ping():
    return jsonify({"message": 'Hello'})

@app.route('/products', methods=['GET'])
def getProducts():
        return jsonify({
            "products": products,
            "message": "listed success"
        })

@app.route('/products/<string:name>', methods=['GET'])
def getProduct(name):
        productFound = [product for product in products if product['name'] == name]
        if (len(productFound) > 0):
            return jsonify({
                'product': productFound[0] 
             })

        return jsonify({
            'error': 'Product not found'
        })

@app.route('/products', methods=['POST'])
def createProduct():
    newProduct = {
        "name": request.json['name'],
        "price:": request.json['price'] ,
        "quantity": request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({
        "products": products,
        "message": "Product added success"
    })

@app.route('/products/<string:name>', methods=['PUT'])
def editProduct(name):
        productFound = [product for product in products if product['name'] == name]
        if (len(productFound) > 0):
            productFound[0]['name'] = request.json['name']
            productFound[0]['price'] = request.json['price']
            productFound[0]['quantity'] = request.json['quantity']
            return jsonify({
                "products": products,
                "message": "Product updated success"
            })
        return jsonify({
            'error': 'Product not found'
        })

@app.route('/products/<string:name>', methods=['DELETE'])
def deleteProduct(name):
        productFound = [product for product in products if product['name'] == name]
        if (len(productFound) > 0):
            products.remove(productFound[0])
            return jsonify({
                "products": products,
                "message": "Product updated success"
            })
        return jsonify({
            'error': 'Product not found'
        })

if __name__ == '__main__':
        app.run(debug=True, port=4000)