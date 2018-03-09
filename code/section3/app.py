from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name':'under-wear',
                'price': 1.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')



# POST - used to receive data from client
# GET - used to sent data to client

# POST /store data:{name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    # print(type(request_data))
    # return jsonify({'message':'Cannot create a new store!'})
    if  request_data is None:
        return jsonify({'message':'Cannot create a new store'})
    else:
        new_store = {
            'name':request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store)



# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores, if any return, if no return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    message = 'store' + str(name) + 'not found'
    return jsonify({'message':message})


# GET /store
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})


# POST /store/<string:name>/item <name:m, price>
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'message':'Succeed'})
    message = 'store' + str(name) + 'not found!'
    return jsonify({'message': message})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            if len(store['items']) > 0:
                return jsonify({'items':store['items']})
            else:  
                return jsonify({'message': 'No Items'})
    message = 'store' + str(name) + 'not found!'
    return jsonify({'message': message})


app.run(port=8000)