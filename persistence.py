import os
from produto import Produto
from pessoa import Garcom
from pedido import Pedido, ItemPedido

# Caminho da pasta onde os arquivos .txt ficam armazenados
DATA_DIR = "data"

# ------------------ PRODUTOS ------------------

def carregar_produtos():
    produtos = {}
    caminho = os.path.join(DATA_DIR, "produtos.txt")

    if not os.path.exists(caminho):
        return produtos

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_, nome, preco = linha.strip().split(";")
            produtos[int(id_)] = Produto(int(id_), nome, float(preco))
    return produtos


def salvar_produto(produto):
    caminho = os.path.join(DATA_DIR, "produtos.txt")
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{produto.id};{produto.nome};{produto.preco}\n")


# ------------------ GARÇONS ------------------

def carregar_garcons():
    garcons = {}
    caminho = os.path.join(DATA_DIR, "garcons.txt")

    if not os.path.exists(caminho):
        return garcons

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_, nome = linha.strip().split(";")
            garcons[int(id_)] = Garcom(int(id_), nome)
    return garcons


def salvar_garcom(garcom):
    caminho = os.path.join(DATA_DIR, "garcons.txt")
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{garcom.id};{garcom.nome}\n")


# ------------------ PEDIDOS ------------------

def carregar_pedidos():
    pedidos = {}
    caminho = os.path.join(DATA_DIR, "pedidos.txt")

    if not os.path.exists(caminho):
        return pedidos

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id_, garcom_id, mesa = linha.strip().split(";")
            pedidos[int(id_)] = Pedido(int(id_), int(garcom_id), mesa)
    return pedidos


def salvar_pedido(pedido):
    caminho = os.path.join(DATA_DIR, "pedidos.txt")
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pedido.id};{pedido.garcom_id};{pedido.mesa}\n")