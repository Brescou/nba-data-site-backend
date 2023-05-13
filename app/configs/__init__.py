from . import development, test, production


def set_app_config_keys(app, settings):
    all_config_vars = dict(
        list(settings.FLASK_VARS.items()) +
        list(settings.FLASK_JWT_VARS.items()) +
        list(settings.DB_CONNECTION.items())
    )

    for key, value in all_config_vars.items():
        app.config[key] = value


def development_config(app):
    set_app_config_keys(app, development)


def testing_config(app):
    set_app_config_keys(app, test)


def production_config(app):
    set_app_config_keys(app, production)


config = {
    'development': development_config,
    'testing': testing_config,
    'production': production_config,
    'default': development_config,
}
