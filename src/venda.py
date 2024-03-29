from produto import Produto
from cliente import Cliente

class Venda:
    def __init__(self, produto, cliente, quantidade):
        self.produto = produto
        self.cliente = cliente
        self.quantidade = quantidade
        self.vendaValida = None
        if quantidade <= produto.quantidade:
            produto.quantidade -= quantidade
            self.vendaValida = True
            return
        else:
            print(f"possui apenas: {produto.quantidade} em estoque")
            self.vendaValida = False
            return

    def valor_venda(self):
        return self.produto.preco * self.quantidade

