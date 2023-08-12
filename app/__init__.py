import os

import flask

from . import extensions, configs


def create_app():
    app = flask.Flask(__name__)
    _config = os.environ.get('FLASK_ENV', 'development')
    configs.config[_config](app)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    extensions.jwt.init_app(app)
    extensions.cors.init_app(app)
    extensions.mongo.init_app(app)
    # extensions.api.init_app(app)


def register_blueprints(app):
    from .api.v1 import v1
    app.register_blueprint(v1, url_prefix='/v1')
