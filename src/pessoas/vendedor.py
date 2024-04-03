from .pessoa import Pessoa
class Vendedor(Pessoa):
    def __init__(self, nome, idade, cadastro,dinheiro):
        super().__init__(nome, idade)
        self.cadastro = cadastro
        self.dinheiro = dinheiro