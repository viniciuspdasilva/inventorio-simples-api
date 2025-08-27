from flask import request
from flask_restx import Namespace, Resource, fields

from src.routes.movimentacao_route import mov_model
from src.service.product_service import ProductService

ns = Namespace('products', description='Product related operations')

product_model = ns.model('Product', {
    'id': fields.Integer(readonly=True, description='id do produto'),
    'name': fields.String(required=True, description='Nome do produto a ser cadastrado'),
    'description': fields.String(description='Descricao do produto'),
    'price': fields.Float(required=True, description='Preço do produto (R$)'),
    'estoque': fields.Integer(required=True, description='Quantidade de estoque do produto'),
    'is_critical': fields.Boolean(description='O produto é critico?'),
})

product_mov_model = ns.inherit(
    'ProductComMovimentacoes',
    product_model,
    {
        'movimentacoes': fields.List(fields.Nested(mov_model)),
    }
)


@ns.route('/')
class ProductList(Resource):
    @ns.marshal_list_with(product_model)
    def get(self):
        return ProductService.list_all_products()

    @ns.expect(product_model, validate=True)
    def post(self):
        p = ProductService.create_product(request.json)
        return {'message': 'Product created successfully', 'id': p.id}, 201


@ns.route('/<int:id>')
class ProductItem(Resource):
    @ns.marshal_with(product_model)
    def get(self, product_id):
        try:
            return ProductService.get_product_by_id(product_id)
        except ValueError as e:
            return {'message': str(e)}, 404

    def delete(self, product_id):
        try:
            ProductService.remove_product(product_id)
        except ValueError as e:
            return {'message': str(e)}, 404


@ns.route('/<int:id>/movimentacoes')
class ProductMovList(Resource):
    @ns.marshal_list_with(mov_model)
    def get(self, product_id):
        product = ProductService.get_product_by_id(product_id)
        return product.movements
