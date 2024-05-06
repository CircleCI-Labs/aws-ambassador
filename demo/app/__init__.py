from flask import Flask
from config import config


# Create a flask app. Pass in a config
def create_app(config_name):
    app = Flask(__name__)

    # Pulls in all our variables set in the config and adds them to the flask app
    app.config.from_object(config[config_name]())
    config[config_name].init_app(app)

    # Adding blueprint from the main folder
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
