class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("João", 100)
conta.depositar(50)
print("Saldo após depósito:", conta.saldo)
conta.sacar(30)
print("Saldo após saque:", conta.saldo)
