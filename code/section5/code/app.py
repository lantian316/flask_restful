from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from usermanage import UserRegister
from items import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
app.secret_key = 'nam'
api = Api(app)
jwt = JWT(app, authenticate, identity)   #/auth



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=3000, debug=True)