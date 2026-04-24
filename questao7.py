class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self._preco = preco

    def getPreco(self):
        return self._preco

    def setPreco(self, novo_preco):
        self._preco = novo_preco

l = Livro("Python Básico", 200, "Autor X", 59.90)
print("Preço atual:", l.getPreco())
l.setPreco(49.90)
print("Novo preço:", l.getPreco())
