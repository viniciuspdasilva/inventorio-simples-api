from flask_restx import Namespace, Resource, fields

from src.service.fornecedor_service import FornecedorService

ns = Namespace('fornecedores', description='Fornecedores de pedido')

fornecedor_model = ns.model('Fornecedor', {
    'id': fields.Integer(readonly=True),
    'cnpj': fields.String(readonly=True),
    'nome': fields.String(required=True),
    'email': fields.String(required=True),
    'telefone': fields.String(),
})

@ns.route('/')
class FornecedorListResource(Resource):
    @ns.marshal_list_with(fornecedor_model)
    def get(self):
        return FornecedorService.listar()
    @ns.expect(fornecedor_model)
    @ns.marshal_with(fornecedor_model, code=201)
    def post(self):
        return FornecedorService.criar(ns.payload), 201