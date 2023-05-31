from flask import g, request
from functools import wraps

from app.auth.actions import validate_token
from app.model.user import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        username = validate_token(token)
        if not username:
            return {'message': 'Invalid or expired token.'}, 403
        user = User.find({'username': username})
        if not user:
            return {'message': 'User not found.'}, 404
        g.current_user = user
        return f(*args, **kwargs)

    return decorated_function
