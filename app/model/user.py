from werkzeug.security import generate_password_hash, check_password_hash

from app.model.base import MongoModel


class User(MongoModel):
    collection_name = 'users'

    @classmethod
    def create(cls, username, password):
        user = {"username": username, "password": generate_password_hash(password)}
        cls.insert(user)

    @property
    def username(self):
        return self.document["username"]

    def check_password(self, password):
        return check_password_hash(self.password, password)
