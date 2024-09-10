class Escola:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self) -> str:
        print(self.nome)