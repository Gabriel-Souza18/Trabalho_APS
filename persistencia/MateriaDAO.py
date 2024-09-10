import json
from modelo.escola.Materia import Materia 

CAMINHO = "persistencia/dados/"

class MateriaDAO:
    def __init__(self, professor_dao):
        self.professor_dao = professor_dao
        self.materias = self.carregar_materias()

    def carregar_materias(self):
        try:
            with open(CAMINHO + "materias.json", 'r', encoding='utf-8') as arquivo:
                materias_data = json.load(arquivo)
                materias = []
                for dados in materias_data:
                    professor = self.professor_dao.buscar_professor(dados['professor'])
                    materia = Materia(
                        dados['nome'],
                        professor,
                        dados['turma'],
                        dados['provas'],
                        dados['trabalhos']
                    )
                    materias.append(materia)
                return materias
        except FileNotFoundError:
            return []

    def buscar_materia_por_nome(self, nome):
        for materia in self.materias:
            if materia.nome == nome:
                return materia
        return None 

    def adicionar_materia(self, materia):
        self.materias[materia.nome] = materia
        self.salvar_materias()

    def remover_materia(self, nome_materia):
        if nome_materia in self.materias:
            del self.materias[nome_materia]
            self.salvar_materias()

    def buscar_materia(self, nome_materia):
        return self.materias.get(nome_materia)
    

