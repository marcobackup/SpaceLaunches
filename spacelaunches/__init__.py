from flask import Flask

from .config import config


def create_app(config_name):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config.get(config_name))

    # Blueprint extension
    from spacelaunches.blueprints.launches.views import launches
    app.register_blueprint(launches, url_prefix='/')

    return app
    
