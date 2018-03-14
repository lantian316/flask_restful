import sqlite3
from user import User
from flask_restful import  Resource, reqparse

class FindUser:

    def __init__(self, db):
        if isinstance(db, str):
            self.db = db
        else:
            db = str(db)
            self.db = db
        self.table = 'users'

    def find_by_username(self, name):
        connection = sqlite3.connect(self.db, check_same_thread=False)
        cursor = connection.cursor()
        query = "SELECT * FROM " + self.table + " WHERE username = ?;"
        result = cursor.execute(query, (name,))
        users = []
        if result:
            for row in result:
                user = User(*row)
                users.append(user)
        else:
            users = None
            connection.close()
        connection.close()
        return users
    
    def find_by_id(self, _id):
        connection = sqlite3.connect(self.db, check_same_thread=False)
        cursor = connection.cursor()
        query = "SELECT * FROM "  + self.table +" WHERE id = ?;"

        result = cursor.execute(query, (_id,))
        users = []
        if result:
            for row in result:
                user = User(*row)
                users.append(user)
        else:
            users = None
            connection.close()
        connection.close()
        return users
        
        
        
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required = True,
                        help = 'This field cannot be blank.')
    parser.add_argument('password',
                        type=str,
                        required = True,
                        help = 'This field cannot be blank.')


    def post(self):

        data = UserRegister.parser.parse_args()

        if not data:
            return {'message':'Bad Request!'},401

        finder = FindUser('data.db')
        if finder.find_by_username(data['username']):
            return {'message':'Duplicated user!'}, 401

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?); "
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message':'User created successfully.'}, 201
