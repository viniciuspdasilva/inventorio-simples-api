from src import db
from src.persistence.models.fornecedores import Fornecedores


class FornecedorDAO:
    @staticmethod
    def list_fornecedores():
        return Fornecedores.query.all()
    @staticmethod
    def get_fornecedor_by_id(id_fornecedor):
        return Fornecedores.query.get(id_fornecedor)
    @staticmethod
    def get_fornecedor_by_email(email):
        return Fornecedores.query.filter_by(email=email).first()
    @staticmethod
    def get_fornecedor_by_cnpj(cnpj):
        return Fornecedores.query.filter_by(cnpj=cnpj).first()
    @staticmethod
    def add_fornecedor(nome, email, telefone, cnpj):
       fornecedores = Fornecedores(nome, email, telefone, cnpj)
       db.session.add(fornecedores)
       db.session.commit()
    @staticmethod
    def delete_fornecedor(id_fornecedor):
        fornecedor = FornecedorDAO.get_fornecedor_by_id(id_fornecedor)
        if fornecedor:
          db.session.delete(fornecedor)
          db.session.commit()
        return fornecedor
