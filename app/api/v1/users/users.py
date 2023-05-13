from flask import request, jsonify
from flask_restful import Resource

from app.model.user import User


class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data["username"] or not data["password"]:
            return jsonify({"message": "Invalid request"}), 400
        user = User.find({"username": data["username"]})
        if user:
            return jsonify({"message": "User already exists"}), 400
        User.create(data["username"], data["password"])
        return jsonify({"message": "User created"}), 201
