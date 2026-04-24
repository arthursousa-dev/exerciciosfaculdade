class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentualDeAumento):
        self.salario *= (1 + porcentualDeAumento/100)

f = Funcionario("Harry", 25000)
f.aumentarSalario(10)
print(f"Novo salário de {f.nome}: {f.salario}")
