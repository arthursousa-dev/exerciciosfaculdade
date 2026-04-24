# Interface simples em linha de comando (View/Controller combinados de forma simples)
# Menu com opções de cadastro e listagem.

from restaurante import Restaurante
from produto import Prato, Bebida, Produto
from pessoa import Garcom

def ler_int(msg, default=None):
    while True:
        try:
            v = input(msg).strip()
            if v=="" and default is not None:
                return default
            return int(v)
        except ValueError:
            print("Digite um número válido.")

def ler_float(msg):
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Digite um número válido (ex: 19.90).")

def menu_principal():
    r = Restaurante()
    while True:
        print("\n--- Restaurante POO (menu) ---")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Cadastrar garçom")
        print("4. Listar garçons")
        print("5. Criar pedido")
        print("6. Adicionar item a pedido")
        print("7. Listar pedidos")
        print("8. Fechar pedido")
        print("9. Sair")
        op = input("Escolha opção: ").strip()
        if op == "1":
            try:
                pid = ler_int("ID do produto: ")
                nome = input("Nome: ").strip()
                preco = ler_float("Preço: ")
                tipo = input("Tipo (p=prato / b=bebida / o=outro): ").strip().lower()
                if tipo == "p":
                    veg = input("Vegetariano? (s/n): ").strip().lower() == "s"
                    p = Prato(pid, nome, preco, vegetariano=veg)
                elif tipo == "b":
                    alc = input("Alcoólico? (s/n): ").strip().lower() == "s"
                    p = Bebida(pid, nome, preco, alcoolica=alc)
                else:
                    p = Produto(pid, nome, preco)
                r.cadastrar_produto(p)
                print("Produto cadastrado com sucesso.")
            except Exception as e:
                print("Erro ao cadastrar produto:", e)

        elif op == "2":
            prods = r.listar_produtos()
            if not prods:
                print("Nenhum produto cadastrado.")
            for p in prods:
                print(p.get_info(), "-", p.descricao())

        elif op == "3":
            try:
                gid = ler_int("ID do garçom: ")
                nome = input("Nome do garçom: ").strip()
                cont = input("Contato: ").strip()
                g = Garcom(gid, nome, cont)
                r.cadastrar_garcom(g)
                print("Garçom cadastrado.")
            except Exception as e:
                print("Erro ao cadastrar garçom:", e)

        elif op == "4":
            gs = r.listar_garcons()
            if not gs:
                print("Nenhum garçom cadastrado.")
            for g in gs:
                print(g.get_info())

        elif op == "5":
            try:
                pid = ler_int("ID do pedido: ")
                gid = ler_int("ID do garçom responsável: ")
                mesa = input("Número/identificação da mesa: ").strip()
                r.criar_pedido(pid, gid, mesa)
                print("Pedido criado.")
            except Exception as e:
                print("Erro ao criar pedido:", e)

        elif op == "6":
            try:
                pedido_id = ler_int("ID do pedido: ")
                produto_id = ler_int("ID do produto: ")
                qtd = ler_int("Quantidade: ", default=1)
                r.adicionar_item_ao_pedido(pedido_id, produto_id, qtd)
                print("Item adicionado ao pedido.")
            except Exception as e:
                print("Erro ao adicionar item:", e)

        elif op == "7":
            pedidos = r.listar_pedidos()
            if not pedidos:
                print("Nenhum pedido registrado.")
            for p in pedidos:
                print("Pedido", p.id, "| Garçom:", p.garcom_id, "| Mesa:", p.mesa, "| Status:", p.status, "| Total: R$", f"{p.total:.2f}")
                for it in p.itens:
                    print(f"  - {it.nome} x{it.quantidade} = R$ {it.subtotal:.2f}")

        elif op == "8":
            try:
                pid = ler_int("ID do pedido a fechar: ")
                r.fechar_pedido(pid)
                print("Pedido fechado.")
            except Exception as e:
                print("Erro ao fechar pedido:", e)

        elif op == "9":
            print("Saindo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()