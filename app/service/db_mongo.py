import flask
from flask import current_app
from pymongo import MongoClient


class Mongo:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)

    def connect(self):
        if 'mongo' not in flask._app_ctx_stack.top:
            flask._app_ctx_stack.top.mongo = MongoClient(current_app.config['MONGODB_URI'])
        return flask._app_ctx_stack.top.mongo

    def teardown(self, exception):
        mongo = getattr(flask._app_ctx_stack.top, 'mongo', None)
        if mongo is not None:
            mongo.close()
