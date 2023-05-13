DB_CONNECTION = {
    "MONGODB_DB": "",
    "MONGODB_USERNAME": "",
    "MONGODB_PASSWORD": "",
    "MONGODB_HOST": "",
    "MONGODB_PORT": None
}

DATABASE_URI = ''

FLASK_VARS = {
    'SECRET_KEY': '',
}

FLASK_JWT_VARS = {
    'JWT_AUTH_URL_RULE': '/api/auth',
}
# MONGO_URI = f"mongodb+srv://{config('DB_USER')}:{config('DB_PASSWORD')}@cluster-uni-work.axy4lk0.mongodb" \
#             f".net/{config('DB_NAME_DEV')}?retryWrites=true&w=majority"