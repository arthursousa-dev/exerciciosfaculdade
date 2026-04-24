class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
        else:
            print("Estoque insuficiente.")

    def repor(self, qtd):
        self.estoque += qtd

p = Produto("Escova", 12.5, 10)
p.vender(3)
print("Estoque após venda:", p.estoque)
p.repor(5)
print("Estoque após reposição:", p.estoque)
