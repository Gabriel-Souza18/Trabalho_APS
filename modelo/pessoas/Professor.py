from .Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, email, registro, salario):
        super().__init__(nome, idade, email)
        self.registro = registro
        self.salario = salario

    def __str__(self):
        return f"Professor(nome={self.nome}, idade={self.idade}, email={self.email}, registro={self.registro}, salario={self.salario})"

    __repr__ = __str__

