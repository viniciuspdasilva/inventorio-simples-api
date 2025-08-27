from flask_restx import Api
from flask import Flask
from .config import Config
from .database import init_app, db
from .routes.product_resource import ns as prod_ns
from .routes.movimentacao_route import ns as mov_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)
    api = Api(
        app,
        version='1.0',
        title='Inventory API',
        description='Inventory API',
        doc='/docs',
        prefix='/api/v1'
    )
    api.add_namespace(prod_ns, path='/products')
    api.add_namespace(mov_ns, path='/movements')

    return app
