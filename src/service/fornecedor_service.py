from src.persistence.dao.fornecedor_dao import FornecedorDAO


class FornecedorService:
    @staticmethod
    def listar():
        return FornecedorDAO.list_fornecedores()

    @staticmethod
    def detalhar(fid):
        f = FornecedorDAO.get_fornecedor_by_id(fid)
        if not f:
            raise ValueError("Fornecedor não encontrado")
        return f

    @staticmethod
    def find_fornecedor_by_cnpj(cnpj):
        f = FornecedorDAO.get_fornecedor_by_cnpj(cnpj)
        if not f:
            raise ValueError(f"Nenhum fornecedor encontrado com esse cnpj %s", cnpj)
        return f

    @staticmethod
    def criar(data):
        return FornecedorDAO.add_fornecedor(**data)

    @staticmethod
    def deletar(fid):
        fornecedor = FornecedorDAO.get_fornecedor_by_id(fid)
        if not fornecedor:
            raise ValueError("Nenhum fornecedor encontrado")
        FornecedorDAO.delete_fornecedor(fid)