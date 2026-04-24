# Modela Pedido e ItemPedido (composição: um Pedido tem ItemPedido(s))

from datetime import datetime

class ItemPedido:
    """Composição dentro de Pedido: representa um item (produto + quantidade)."""
    def __init__(self, produto_id: int, nome: str, preco_unit: float, quantidade: int =1):
        self.produto_id = int(produto_id)
        self.nome = nome
        self.preco_unit = float(preco_unit)
        self.quantidade = int(quantidade)

    @property
    def subtotal(self) -> float:
        return self.preco_unit * self.quantidade

    def to_line(self) -> str:
        """Formato para persistência em texto."""
        return f"{self.produto_id}:{self.nome}:{self.preco_unit:.2f}:{self.quantidade}"

    @staticmethod
    def from_line(line: str):
        prod_id, nome, preco, qtd = line.split(":")
        return ItemPedido(int(prod_id), nome, float(preco), int(qtd))

class Pedido:
    """Representa um pedido. Agrega produtos via ItemPedido e referencia um Garcom (agregação)."""
    def __init__(self, pedido_id: int, garcom_id: int, mesa: str):
        self.id = int(pedido_id)
        self.garcom_id = int(garcom_id)   # agregação: apenas referência
        self.mesa = mesa
        self.itens = []  # lista de ItemPedido (composição)
        self.status = "ABERTO"  # ABERTO, FECHADO, CANCELADO
        self.created_at = datetime.now()

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)

    def remover_item(self, produto_id: int):
        self.itens = [i for i in self.itens if i.produto_id != int(produto_id)]

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.itens)

    def fechar(self):
        if not self.itens:
            raise ValueError("Não é possível fechar pedido sem itens.")
        self.status = "FECHADO"

    def cancelar(self):
        self.status = "CANCELADO"

    def to_line(self) -> str:
        """Serializa o pedido para uma linha: campos separados e itens separados por |"""
        itens_str = "|".join([i.to_line() for i in self.itens])
        created = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.id};{self.garcom_id};{self.mesa};{self.status};{created};{self.total:.2f};{itens_str}"

    @staticmethod
    def from_line(line: str):
        if not line.strip():
            return None
        parts = line.strip().split(";")
        pid = int(parts[0])
        garcom_id = int(parts[1])
        mesa = parts[2]
        status = parts[3]
        created = parts[4]
        total = float(parts[5])
        itens_part = parts[6] if len(parts) > 6 else ""
        pedido = Pedido(pid, garcom_id, mesa)
        pedido.status = status
        # parse itens
        if itens_part:
            itens_raw = itens_part.split("|")
            for ir in itens_raw:
                item = ItemPedido.from_line(ir)
                pedido.adicionar_item(item)
        return pedido