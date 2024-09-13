import json
from modelo.escola.Materia import Materia
from persistencia.BaseDAO import BaseDAO

class MateriaDAO(BaseDAO):
    def __init__(self, professor_dao, turma_dao):
        super().__init__("materias.json")
        self.professor_dao = professor_dao
        self.turma_dao = turma_dao
        self.materias = self.carregar_materias()

    def carregar_materias(self):
        materias = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                if isinstance(dados, list):
                    for item in dados:
                        professor = self.professor_dao.buscar_professor_por_nome(item['professor'])
                        turma = self.turma_dao.buscar_turma(item['turma'])
                        materia = Materia(
                            nome=item['nome'],
                            professor=professor,
                            turma=turma,
                            provas=item.get('provas', {}),
                            trabalhos=item.get('trabalhos', {})
                        )
                        materias.append(materia)
                elif isinstance(dados, dict):
                    for nome, item in dados.items():
                        professor = self.professor_dao.buscar_professor_por_nome(item['professor'])
                        turma = self.turma_dao.buscar_turma(item['turma'])
                        materia = Materia(
                            nome=item['nome'],
                            professor=professor,
                            turma=turma,
                            provas=item.get('provas', {}),
                            trabalhos=item.get('trabalhos', {})
                        )
                        materias.append(materia)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao carregar dados: arquivo JSON malformado.")
        return materias

    def salvar_dados(self):
        dados_para_salvar = {materia.nome: {
            "nome": materia.nome,
            "professor": materia.professor.registro if materia.professor else None,
            "turma": materia.turma.nome_turma if materia.turma else None,
            "provas": materia.provas,
            "trabalhos": materia.trabalhos
        } for materia in self.materias}
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(dados_para_salvar, file, indent=4, ensure_ascii=False)

    def adicionar_materia(self, materia: Materia):
        self.add_item(materia.nome, {
            "nome": materia.nome,
            "professor": materia.professor.nome if materia.professor else None,
            "turma": materia.turma.nome_turma if materia.turma else None,
            "provas": materia.provas,
            "trabalhos": materia.trabalhos
        })
        self.materias = self.carregar_materias()

    def remover_materia(self, nome_materia):
        self.remove_item(nome_materia)
        self.materias = self.carregar_materias()

    def buscar_materia(self, nome_materia):
        for materia in self.materias:
            if materia.nome == nome_materia:
                return materia
        return None  

    def buscar_materias(self):
        return self.materias

    def buscar_materias_por_professor(self, registro_professor):
        return [materia for materia in self.materias if materia.professor and materia.professor.registro == registro_professor]

    def buscar_materia_por_nome(self, nome):
        for materia in self.materias:
            if materia.nome == nome:
                return materia
        return None
