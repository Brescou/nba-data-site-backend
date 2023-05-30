import flask
from flask import current_app
from pymongo import MongoClient

class Mongo:
    def __init__(self, app=None):
        self._mongo = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)
        app.mongo = self

    @property
    def client(self):
        ctx = flask._app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mongo'):
                ctx.mongo = MongoClient(current_app.config['MONGODB_URI'])
                ctx.db = ctx.mongo[current_app.config['MONGODB_DB']]
            return ctx.db
        else:
            raise RuntimeError('Outside of application context.')

    def teardown(self, exception):
        ctx = flask._app_ctx_stack.top
        if ctx is not None and hasattr(ctx, 'mongo'):
            ctx.mongo.close()
