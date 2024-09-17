from flask import request, jsonify
from flask_restful import Resource

from app.model.user import User


class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data["username"] or not data["password"] or not data["email"]:
            return jsonify({"message": "Invalid request"}), 400
        user = User.find({"username": data["username"]})
        if user:
            return jsonify({"message": "Username already exists"}), 400
        user = User.find({"email": data["email"]})
        if user:
            return jsonify({"message": "Email already exists"}), 400
        User.create(username=data["username"], email=data["email"], password=data["password"])
        return jsonify({"message": "User created"}), 201
