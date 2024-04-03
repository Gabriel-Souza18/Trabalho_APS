from .pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, CPF):
        super().__init__(nome, idade)
        self.CPF = CPF
