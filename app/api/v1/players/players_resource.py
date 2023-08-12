from flask import request, jsonify
from flask_restful import Resource


class Players(Resource):
    def get(self):
        return jsonify({'message': 'Hello, World!'})


class Player(Resource):
    def get(self, player_id):
        return jsonify({'message': 'Hello, World!'})
