from flask_restx import Api
from flask import Flask
from .config import Config
from .database import init_app, db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)
    api = Api(app, version='1.0', title='Inventory API', description='Inventory API')

    return app
