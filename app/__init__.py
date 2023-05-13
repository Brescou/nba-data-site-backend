import flask
from . import extensions, configs
from .api.v1 import v1
from flask import url_for


def create_app(config_name='default'):
    app = flask.Flask(__name__)
    configs.config[config_name](app)
    app.register_blueprint(v1, url_prefix='/v1')
    register_extensions(app)
    return app

def register_extensions(app):
    extensions.jwt.init_app(app)
    extensions.cors.init_app(app)
    extensions.mongo.init_app(app)
    extensions.api.init_app(app)
