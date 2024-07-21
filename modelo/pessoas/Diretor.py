from .Pessoa import Pessoa

class Diretor(Pessoa):
    def __init__(self, nome, idade, email, registro, salario):
        super().__init__(nome, idade, email)
        self.registro = registro
        self.salario = salario
        