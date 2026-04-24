#simula um saque. Se o valor for maior que o saldo, o sistema não permite.

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

try:
    saldo = float(input("Informe seu saldo atual: "))
    valor = float(input("Informe o valor do saque: "))
    saldo = sacar(saldo, valor)
    print(f"Saque realizado! Seu novo saldo é: R$ {saldo:.2f}")
except ValueError as e:
    print(e)
