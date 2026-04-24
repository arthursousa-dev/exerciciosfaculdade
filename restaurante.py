# Classe que agrega garcons, produtos e pedidos. Fornece operações de negócio.

from persistence import carregar_produtos, carregar_garcons, carregar_pedidos, salvar_produto, salvar_garcom, salvar_pedido
from produto import Produto, Prato, Bebida
from pessoa import Garcom
from pedido import Pedido, ItemPedido


class Restaurante:
    """Agrega garçons, produtos e pedidos. Controla operações principais."""
    def __init__(self):
        # Carrega do disco (persistência)
        self.produtos = carregar_produtos()  #  id->Produto
        self.garcons = carregar_garcons()    #  id->Garcom
        self.pedidos = carregar_pedidos()    #  id->Pedido

    # ---------- Produtos ----------
    def listar_produtos(self):
        return list(self.produtos.values())

    def cadastrar_produto(self, produto: Produto):
        if produto.id in self.produtos:
            raise KeyError("ID do produto já cadastrado.")
        self.produtos[produto.id] = produto
        salvar_produto(produto)

    # ---------- Garçons ----------
    def listar_garcons(self):
        return list(self.garcons.values())

    def cadastrar_garcom(self, garcom: Garcom):
        if garcom.id in self.garcons:
            raise KeyError("ID do garçom já cadastrado.")
        self.garcons[garcom.id] = garcom
        salvar_garcom(garcom)

    # ---------- Pedidos ----------
    def criar_pedido(self, pedido_id: int, garcom_id: int, mesa: str) -> Pedido:
        if pedido_id in self.pedidos:
            raise KeyError("ID de pedido já existe.")
        if garcom_id not in self.garcons:
            raise KeyError("Garçom não existe.")
        p = Pedido(pedido_id, garcom_id, mesa)
        self.pedidos[p.id] = p
        # persistir pedido apenas ao salvar (evitar linhas incompletas)
        salvar_pedido(p)
        return p

    def adicionar_item_ao_pedido(self, pedido_id: int, produto_id: int, quantidade: int=1):
        if pedido_id not in self.pedidos:
            raise KeyError("Pedido não encontrado.")
        if produto_id not in self.produtos:
            raise KeyError("Produto não encontrado.")
        produto = self.produtos[produto_id]
        item = ItemPedido(produto.id, produto.nome, produto.preco, quantidade)
        pedido = self.pedidos[pedido_id]
        pedido.adicionar_item(item)
        # rewrite pedido file (simples estratégia: regravar tudo)
        self._persistir_todos_pedidos()

    def fechar_pedido(self, pedido_id: int):
        if pedido_id not in self.pedidos:
            raise KeyError("Pedido não encontrado.")
        pedido = self.pedidos[pedido_id]
        pedido.fechar()
        self._persistir_todos_pedidos()

    def listar_pedidos(self):
        return list(self.pedidos.values())

    def _persistir_todos_pedidos(self):
        # regrava todos os pedidos no arquivo (sobrescreve)
        from persistence import PEDIDO_FILE, ensure_data_dir
        ensure_data_dir()
        with open(PEDIDO_FILE, "w", encoding="utf-8") as f:
            for p in self.pedidos.values():
                f.write(p.to_line() + "\n")