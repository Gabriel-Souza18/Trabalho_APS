import json
from persistencia.BaseDAO import BaseDAO
from modelo.pessoas.Aluno import Aluno

class AlunoDAO(BaseDAO):
    def __init__(self):
        super().__init__("alunos.json")
        self.alunos = self.carregar_alunos()

    def carregar_alunos(self):
        alunos = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                if isinstance(dados, list):
                    for item in dados:
                        aluno = Aluno(
                            nome=item['nome'],
                            idade=item['idade'],
                            email=item['email'],
                            matricula=item['matricula'],
                            turma=item['turma'],
                            notas=item.get('notas', {})  # 'notas' pode ser opcional
                        )
                        alunos[aluno.matricula] = aluno
                elif isinstance(dados, dict):
                    for matricula, item in dados.items():
                        aluno = Aluno(
                            nome=item['nome'],
                            idade=item['idade'],
                            email=item['email'],
                            matricula=item['matricula'],
                            turma=item['turma'],
                            notas=item.get('notas', {})
                        )
                        alunos[matricula] = aluno
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            print("Erro ao carregar alunos: arquivo JSON está malformado")
            self.data = {}
        return alunos

    def salvar_dados(self):
        dados_para_salvar = {mat: {
            "nome": aluno.nome,
            "idade": aluno.idade,
            "email": aluno.email,
            "matricula": aluno.matricula,
            "turma": aluno.turma,
            "notas": aluno.notas
        } for mat, aluno in self.alunos.items()}
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(dados_para_salvar, file, indent=4, ensure_ascii=False)

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos[aluno.matricula] = aluno
        self.salvar_dados()  # Salvar alterações no arquivo JSON

    def remover_aluno(self, matricula):
        if matricula in self.alunos:
            del self.alunos[matricula]
            self.salvar_dados()  # Salvar alterações no arquivo JSON

    def buscar_aluno(self, matricula):
        return self.alunos.get(matricula)

    def buscar_alunos(self):
        return self.alunos.values()

    def buscar_aluno_por_nome(self, nome):
        resultados = [aluno for aluno in self.alunos.values() if aluno.nome.lower() == nome.lower()]
        return resultados
