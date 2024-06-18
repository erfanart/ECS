from flask import Flask,current_app
from config import config
import logging
import os
from .views import main_blueprint

def create_app(config_name):
    app = Flask(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    with app.app_context():
        current_app.logger.addHandler(handler)
        current_app.register_blueprint(main_blueprint)
        current_app.config.from_object(config[config_name])
        current_app.logger.setLevel(logging.DEBUG)  
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  

    return app


def configure_logging(app):
    # Configure logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)