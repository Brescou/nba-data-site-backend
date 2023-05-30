from marshmallow import Schema, fields, validate, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

from app.model.base import MongoModel


class User(MongoModel):
    collection_name = 'users'

    @classmethod
    def create(cls, username, email, password):
        user = {"username": username, "email": email, "password": generate_password_hash(password)}
        cls.insert(user)

    @property
    def username(self):
        return self.document["username"]

    @property
    def password(self):
        return self.document.get("password")

    @property
    def email(self):
        return self.document.get("email")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def check_username_exist(cls, username):
        return cls.find({"username": username})

    @classmethod
    def check_email_exist(cls, email):
        return cls.find({"email": email})


def validate_password(password):
    if len(password) < 6:
        raise ValidationError('Password must be at least 6 characters long.')
    elif " " in password:
        raise ValidationError('Password must not contain spaces.')
    elif not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least 1 digit.')
    elif not any(char.isalpha() for char in password):
        raise ValidationError('Password must contain at least 1 letter.')


def validate_username(username):
    if len(username) < 3:
        raise ValidationError('Username must be at least 6 characters long.')
    elif User.check_username_exist(username):
        raise ValidationError('Username already exist.')
    elif " " in username:
        raise ValidationError('Username must not contain spaces.')
    elif not username.isalnum():
        raise ValidationError('Username must not contain special characters.')


def validate_email(email):
    if len(email) < 6:
        raise ValidationError('Email must be at least 6 characters long.')
    elif User.check_email_exist(email):
        raise ValidationError('Email already exist.')
    elif "@" not in email:
        raise ValidationError('Invalid email.')


class UserSchema(Schema):
    username = fields.Str(required=True, validate=(validate.Length(min=3), validate_username))
    password = fields.Str(required=True, validate=(validate.Length(min=1), validate_password))
    email = fields.Email(required=True, validate=(validate.Length(min=1), validate_email))
