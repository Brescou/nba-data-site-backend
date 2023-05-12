from decouple import config


class Config(object):
    JWT_SECRET_KEY = "your-secret-key"


class DevelopmentConfig(Config):
    MONGO_URI = f"mongodb+srv://{config('DB_USER_DEV')}:{config('DB_PASSWORD_DEV')}@cluster-uni-work.axy4lk0.mongodb.net/{config('DB_NAME_DEV')}?retryWrites=true&w=majority"
    DEBUG = True


class ProductionConfig(Config):
    MONGO_URI = f"mongodb+srv://{config('DB_USER')}:{config('DB_PASSWORD')}@cluster-uni-work.axy4lk0.mongodb.net/{config('DB_NAME_DEV')}?retryWrites=true&w=majority"
    DEBUG = False
