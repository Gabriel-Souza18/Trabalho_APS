from pessoa import Pessoa
class Vendedor(Pessoa):
    def __init__(self, nome, idade, cadastro):
        super().__init__(nome, idade)
        self.cadastro = cadastro
        self.dinheiro = 0