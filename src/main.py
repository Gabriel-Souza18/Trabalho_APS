from produto import Produto
from cliente import Cliente
from venda import Venda
from estoque import Estoque

andre = Cliente("Andre", "1235483456")
estoque = Estoque()
'''
estoque.adicionar_produto('banana', 10.50, 12)
estoque.adicionar_produto('maca', 5, 18)
estoque.adicionar_produto('goiaba', 4.2, 15)
estoque.salvar_arquivo()
'''

estoque.ler_arquivo()
estoque.imprimir_estoque()

venda = Venda(andre, estoque)
venda.vender_produtos('banana', 1)
venda.vender_produtos('maca', 50)
venda.vender_produtos('abacaxi', 3)

print('Valor total: '+ str(venda.valor_venda()))
