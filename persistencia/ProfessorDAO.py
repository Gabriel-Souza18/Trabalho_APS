import json
from modelo.pessoas.Professor import Professor
from persistencia.BaseDAO import BaseDAO

class ProfessorDAO(BaseDAO):
    def __init__(self):
        super().__init__("professores.json")
        self.professores = self.carregar_professores()

    def carregar_professores(self):
        professores = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                if isinstance(dados, list):
                    for item in dados:
                        professor = Professor(
                            nome=item['nome'],
                            idade=item['idade'],
                            email=item['email'],
                            registro=item['registro'],
                            salario=item['salario']
                        )
                        professores[professor.registro] = professor
                elif isinstance(dados, dict):
                    for registro, item in dados.items():
                        professor = Professor(
                            nome=item['nome'],
                            idade=item['idade'],
                            email=item['email'],
                            registro=item['registro'],
                            salario=item['salario']
                        )
                        professores[registro] = professor
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            print("Erro ao carregar professores: arquivo JSON está malformado")
            self.data = {}
        return professores

    def salvar_dados(self):
        dados_para_salvar = {reg: {
            "nome": prof.nome,
            "idade": prof.idade,
            "email": prof.email,
            "registro": prof.registro,
            "salario": prof.salario
        } for reg, prof in self.professores.items()}
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(dados_para_salvar, file, indent=4, ensure_ascii=False)

    def adicionar_professor(self, professor: Professor):
        self.professores[professor.registro] = professor
        self.salvar_dados()  # Salvar alterações no arquivo JSON

    def remover_professor(self, registro):
        if registro in self.professores:
            del self.professores[registro]
            self.salvar_dados()  # Salvar alterações no arquivo JSON

    def buscar_professor(self, registro):
        return self.professores.get(registro)

    def buscar_professores(self):
        return self.professores.values()

    def buscar_professor_por_nome(self, nome):
        for professor in self.professores.values():
            if professor.nome == nome:
                return professor
        return None
