from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {
        'id': 1,
        'title': 'Drumkit',
        'description': 'A nice drumkit',
        'price': 525.99,
        'image': 'https://www.rockemmusic.com/files/imagecache/product_full/product-images/LCEE20028_D.jpg'
    },
    {
        'id': 2,
        'title': 'Ukulele',
        'description': 'A soprano ukulele',
        'price': 109.99,
        'image': 'https://musiciselementary.com/wp-content/uploads/2016/01/ka-15s.jpg'
    },
    {
        'id': 3,
        'title': 'Keyboard',
        'description': 'A keyboard for beginners',
        'price': 219.99,
        'image': 'https://i5.walmartimages.com/asr/82459887-b2b5-4f98-8869-4866dbdb96d4_1.8a9d79c8032fbd771261f09c0f3ba850.jpeg'
    }
]

@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'GET':
        return jsonify({'products': products})

    if request.method == 'POST':
        product = {
            'id': products[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json['description'],
            'price': request.json['price'],
            'image': request.json['image']
        }
        products.append(product)
        return jsonify({'product': product}), 201

@app.route('/product/<int:product_id>', methods=['GET', 'DELETE'])
def manage_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'error': 'Product not found here'})

    if request.method == 'GET':
        return jsonify({'product': product[0]})

    if request.method == 'DELETE':
        products.remove(product[0])
        return jsonify({'result': 'Product deleted'})

app.run(port=8080, debug=True)

if __name__ == '__main__':
    app.run(debug=True)