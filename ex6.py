#  criar uma classe para um aluno e um sistema para cadastrar, listar e remover alunos.

class Aluno:
    def __init__(self, nome, ra, email, curso, turma):
        # informações do aluno
        self.nome = nome
        self.ra = ra
        self.email = email
        self.curso = curso
        self.turma = turma

    def __str__(self):
        #  como o aluno será salvo no arquivo (tudo em uma linha separada por vírgulas)
        return f"{self.nome},{self.ra},{self.email},{self.curso},{self.turma}\n"


class CadastroAlunos:
    ARQUIVO = "alunos.txt"  # Nome qe o arquivo será salvo

   
    def cadastrar():
        # Cadastra um novo aluno
        try:
            print("=== CADASTRO DE ALUNO ===")
            nome = input("Nome: ")
            ra = input("RA: ")
            email = input("Email: ")
            curso = input("Curso: ")
            turma = input("Turma: ")

            aluno = Aluno(nome, ra, email, curso, turma)
            with open(CadastroAlunos.ARQUIVO, "a", encoding="utf-8") as f:
                f.write(str(aluno))
            print("Aluno cadastrado com sucesso!")
        except Exception as e:
            print("Erro ao cadastrar aluno:", e)

    
    def listar():
        # Mostra todos os alunos cadastrados
        try:
            with open(CadastroAlunos.ARQUIVO, "r", encoding="utf-8") as f:
                print("=== ALUNOS CADASTRADOS ===")
                print(f.read())
        except FileNotFoundError:
            print("Nenhum aluno cadastrado ainda (arquivo não encontrado).")

    
    def remover(ra):
        # Remove um aluno pelo RA
        try:
            with open(CadastroAlunos.ARQUIVO, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            with open(CadastroAlunos.ARQUIVO, "w", encoding="utf-8") as f:
                for linha in linhas:
                    if ra not in linha:
                        f.write(linha)
            print(f"Aluno com RA {ra} removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover aluno: {e}")
