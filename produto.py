# Modela produtos do restaurante. 
class Produto:
    """Classe base para um produto do restaurante."""
    def __init__(self, produto_id: int, nome: str, preco: float):
        self._id = int(produto_id)
        self._nome = nome
        self._preco = float(preco)

    # Encapsulamento por propriedades
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def get_info(self) -> str:
        """Retorna string descrevendo o produto (polimorfismo em subclasses)."""
        return f"{self._id}|{self._nome}|{self._preco:.2f}"

    def descricao(self) -> str:
        """Descrição legível ao usuário (pode ser sobrescrita)."""
        return f"{self._nome} - R$ {self._preco:.2f}"

class Prato(Produto):
    def __init__(self, produto_id: int, nome: str, preco: float, vegetariano: bool=False):
        super().__init__(produto_id, nome, preco)
        self.vegetariano = vegetariano

    def descricao(self) -> str:
        tag = " (Vegetariano)" if self.vegetariano else ""
        return f"{self.nome}{tag} - R$ {self.preco:.2f}"

class Bebida(Produto):
    def __init__(self, produto_id: int, nome: str, preco: float, alcoolica: bool=False):
        super().__init__(produto_id, nome, preco)
        self.alcoolica = alcoolica

    def descricao(self) -> str:
        tag = " (Alcoólica)" if self.alcoolica else ""
        return f"{self.nome}{tag} - R$ {self.preco:.2f}"