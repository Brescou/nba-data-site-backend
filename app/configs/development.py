import datetime

from decouple import config

DB_CONNECTION = {
    "MONGODB_DB": config('DB_NAME_DEV'),
    "MONGODB_USERNAME": 'root',
    "MONGODB_PASSWORD": 'example',
    "MONGODB_HOST":'localhost',
    "MONGODB_PORT": 27017,
    "MONGODB_URI":'mongodb://root:example@localhost:27017'
    }

FLASK_VARS = {
    'DEBUG': True,
    'SECRET_KEY': 'SecretKey',
}

# flask-jwt vars
FLASK_JWT_VARS = {
    'JWT_AUTH_URL_RULE': '/api/auth',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7)
}
