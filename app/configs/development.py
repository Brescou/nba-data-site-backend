import datetime
from decouple import config

DB_CONNECTION = {
    "MONGODB_DB": config('DB_NAME_DEV'),
    "MONGODB_USERNAME": config('DB_USER_DEV'),
    "MONGODB_PASSWORD": config('DB_PASSWORD_DEV'),
    "MONGODB_HOST": config('MONGODB_HOST'),
    "MONGODB_PORT": 27017,
    "MONGODB_URI": f"mongodb+srv://{config('DB_USER_DEV')}:{config('DB_PASSWORD_DEV')}@cluster-uni-work" \
                   f".axy4lk0.mongodb.net/{config('DB_NAME_DEV')}?retryWrites=true&w=majority",
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
