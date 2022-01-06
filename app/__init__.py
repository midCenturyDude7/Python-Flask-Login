from flask import Flask
from flask_bootstrap import Bootstrap
from config import *


bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    DevelopmentConfig.init_app(app)

    bootstrap.init_app(app)

    return app