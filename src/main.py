from produto import Produto
from cliente import Cliente
from venda import Venda

andre = Cliente("Andre", "1235483456")
banana = Produto('banana', 7.40, 10)

venda = Venda(banana, andre, 11)
if venda.vendaValida:
    print(f'valor da venda :R$ {venda.valor_venda()}')
else:
    print("VendaInvalida")