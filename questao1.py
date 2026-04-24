class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")

p1 = Pessoa("Ana", 25, "Dentista")
p2 = Pessoa("Carlos", 40, "Atendente")
p1.apresentar()
p2.apresentar()
