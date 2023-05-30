import datetime

import jwt
from flask import request, current_app
from flask_restful import Resource
from marshmallow import ValidationError

from app.api.v1 import api
from app.model.user import User, UserSchema


class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return {'message': 'Must provide username and password.'}, 400
        user = User.find({'username': data['username']})
        if not user or not user.check_password(data['password']):
            return {'message': 'Invalid username or password.'}, 400
        token = jwt.encode(
            {'username': user.username, 'exp': datetime.datetime.utcnow() +
                                               datetime.timedelta(days=7)},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return {'message': 'Logged in successfully.', 'token': token}, 200


class Register(Resource):
    def post(self):
        data = request.get_json()
        user_schema = UserSchema()
        try:
            valid_data = user_schema.load(data)
        except ValidationError as err:
            return {'messages': 'Invalid data', 'errors': err.messages}, 400
        user = User()
        user.create(data['username'], data['email'], data['password'])
        return {'message': 'User created successfully.'}, 200


api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
