import json
from modelo.escola.Materia import Materia
from persistencia.BaseDAO import BaseDAO

class MateriaDAO(BaseDAO):
    def __init__(self, professor_dao):
        super().__init__("materias.json")
        self.professor_dao = professor_dao
        self.materias = self.carregar_materias()

    def carregar_materias(self):
        materias = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                self.data = json.load(arquivo)
                for dados in self.data:
                    professor = self.professor_dao.buscar_professor(dados['professor'])
                    materia = Materia(
                        dados['nome'],
                        professor,
                        dados['turma'],
                        dados['provas'],
                        dados['trabalhos']
                    )
                    materias[materia.nome] = materia
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Erro ao carregar materias: arquivo JSON está malformado")
            self.data = []
        return materias

    def adicionar_materia(self, materia: Materia):
        self.add_item(materia.nome, {
            "nome": materia.nome,
            "professor": materia.professor.registro,
            "turma": materia.turma,
            "provas": materia.provas,
            "trabalhos": materia.trabalhos
        })
        self.materias = self.carregar_materias()

    def remover_materia(self, nome_materia):
        self.remove_item(nome_materia)
        self.materias = self.carregar_materias()

    def buscar_materia(self, nome_materia):
        return self.materias.get(nome_materia)

    def buscar_materia_por_nome(self, nome):
        for materia in self.materias.values():
            if materia.nome == nome:
                return materia
        return None