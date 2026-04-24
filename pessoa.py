# Define Pessoa e Garcom (herança). Garcom será agregado no Restaurante.

class Pessoa:
    """Pessoa genérica - serve de base para herança."""
    def __init__(self, nome: str, contato: str):
        self._nome = nome
        self._contato = contato

    @property
    def nome(self):
        return self._nome

    @property
    def contato(self):
        return self._contato

class Garcom(Pessoa):
    """Garçom que serve mesas. Herda de Pessoa."""
    def __init__(self, garcom_id: int, nome: str, contato: str):
        super().__init__(nome, contato)
        self._id = int(garcom_id)
        self._ativo = True  # status

    @property
    def id(self):
        return self._id

    @property
    def ativo(self):
        return self._ativo

    def inativar(self):
        self._ativo = False

    def ativar(self):
        self._ativo = True

    def get_info(self) -> str:
        return f"{self._id}|{self._nome}|{self._contato}|{int(self._ativo)}"