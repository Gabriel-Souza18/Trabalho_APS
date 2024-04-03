from pessoas import *
from venda import *
class Venda:
    def __init__(self, cliente, estoque):
        self.produtos={}
        self.cliente = cliente
        self.estoque = estoque

    def vender_produtos(self, nome_produto, quantidade):
        # Verifica se o produto existe no estoque
        if nome_produto in self.estoque.produtos:
            produto = self.estoque.produtos[nome_produto]
            # Verifica se a quantidade desejada está disponível
            if quantidade <= produto.quantidade:
                # Adiciona o produto à venda
                self.produtos[nome_produto] = (produto, quantidade)
                # Atualiza a quantidade do produto no estoque
                produto.quantidade -= quantidade
            else:
                print(f"Desculpe, só temos {produto.quantidade} unidades do produto {nome_produto} em estoque.")
        else:
            print(f"Desculpe, o produto {nome_produto} não está disponível em nosso estoque.")

    def valor_venda(self):
        total = 0
        # Calcula o valor total da venda
        for produto, quantidade in self.produtos.values():
            total += produto.preco * quantidade
        return total