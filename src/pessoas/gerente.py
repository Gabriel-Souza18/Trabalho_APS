from .vendedor import Vendedor
from .pessoa import Pessoa
class Gerente(Pessoa):
    def __init__(self, nome, idade, cadastro):
        super().__init__(nome, idade)
        self.cadastro = cadastro
        self.vendedores = []

    def escrever_vendedores(self):
        with open("Vendedores.txt", "w") as arq:
            for vendedor in self.vendedores:
                arq.write(f'{vendedor.nome}, {vendedor.idade}, {vendedor.cadastro}, {vendedor.dinheiro}\n')


    def ler_vendedores(self):
        with open("Vendedores.txt", "r") as arq:
            for linha in arq:
                nome, cadastro,idade, dinheiro = linha.strip().split(', ')
                self.adicionar_vendedor( nome, cadastro, idade, dinheiro)

    def adicionar_vendedor(self, nome, idade, cadastro, dinheiro):
        novo_vendedor = Vendedor(nome, idade, cadastro, dinheiro)
        self.vendedores.append(novo_vendedor)
        self.escrever_vendedores()


    def listar_vendedores(self):
        for vendedor in self.vendedores:
            print(vendedor.nome)
    

    
