import datetime

import jwt
from flask import current_app


def create_token(user):
    token = jwt.encode(
        {'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)},
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    user.add_token(token)
    return token


def validate_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['username']
    except jwt.ExpiredSignatureError:

        return 'Token expired, please log in again.'
    except:
        return 'Token is invalid.'
