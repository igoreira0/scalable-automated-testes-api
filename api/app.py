from flask import Flask
from flask_cors import CORS
from .blueprints.health import health_api
from .blueprints.tests import test_api


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(health_api, url_prefix='/api/health')
    app.register_blueprint(test_api, url_prefix='/api/tests')


    return app