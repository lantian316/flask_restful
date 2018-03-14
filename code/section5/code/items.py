import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

db = 'data.db'

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect(db)
        cursor= connection.cursor()

        query = 'SELECT * FROM items WHERE name = ?;'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'id':row[0], 'name':row[1], 'price':row[2]}}
        else:
            return None


    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item,200
        else:
            return {'message':'Can not find item!'}, 400



    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {'message':'Duplicated item in database'}, 401
        data = Item.parser.parse_args()
        if data:
            item = {'name':name, 'price':data['price']}
            items.append(item)
            return item, 201
        return 400

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'Deleted'}


    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}