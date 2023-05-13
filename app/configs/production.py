import datetime

from decouple import config

DB_CONNECTION = {
    "MONGODB_DB": config('DB_NAME_DEV'),
    "MONGODB_USERNAME": config('DB_USER_DEV'),
    "MONGODB_PASSWORD": config('DB_PASSWORD_DEV'),
    "MONGODB_HOST": config('MONGODB_HOST'),
    "MONGODB_PORT": 27017,
    "MONGODB_URI": f"mongodb+srv://{config('DB_USER')}:{config('DB_PASSWORD')}@cluster-uni-work.axy4lk0" \
                   f".mongodb.net/{config('DB_NAME_DEV')}?retryWrites=true&w=majority"
}

FLASK_VARS = {
    'SECRET_KEY': 'SecretKey',
}

FLASK_JWT_VARS = {
    'JWT_AUTH_URL_RULE': '/api/auth',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7)
}
