# Exercícios de Python - Resolução
# =========================================
# Este arquivo contém as soluções para os exercícios das aulas 01 a 04

# =========================================
# AULA 01 - FUNÇÕES
# =========================================

# 1 - Função que recebe 3 argumentos e imprime o produto
def produto(a, b, c):
    print("Produto:", a * b * c)

# 2 - Função para exponenciação
def exponenciacao(base, expoente):
    return base ** expoente

# 3 - Função que imprime a quantidade de dígitos de um número inteiro
def quantidade_digitos(numero):
    print("Quantidade de dígitos:", len(str(abs(numero))))

# 4 - Função que retorna 'P' se positivo e 'N' se negativo
def positivo_ou_negativo(valor):
    return 'P' if valor >= 0 else 'N'

# 5 - Função somaImposto
def somaImposto(taxaImposto, custo):
    return custo * (1 + taxaImposto / 100)

# 6 - Função para gerar tabela de preços (1 a 50)
def tabela_precos():
    for i in range(1, 51):
        print(f"{i} - R$ {i * 1.99:.2f}")

# 7 - Função de cálculo de salário
def calcular_salario(horas_trabalhadas, salario_base=40*10):  # supondo 10 reais/hora
    valor_hora = salario_base / 40
    if horas_trabalhadas > 40:
        extra = horas_trabalhadas - 40
        return salario_base + (extra * valor_hora * 1.5)
    return horas_trabalhadas * valor_hora

# 8 - Função do pescador
def multa_pescador(peso_peixes):
    excesso = max(0, peso_peixes - 50)
    multa = excesso * 4
    return excesso, multa

# 9 - Função calcularTempo
def calcularTempo(minutos):
    if minutos < 15:
        return 0
    horas = minutos / 60
    valor = 9 + max(0, horas - 1) * 1.5
    return valor

def calcularTempoComImpostos(minutos):
    valor = calcularTempo(minutos)
    total = valor * (1 + 0.0033 + 0.0020 + 0.17)
    return total

# 10 - Simulação de financiamento
def simular_financiamento(valor_veiculo, entrada, taxa_juros, parcelas):
    valor_financiado = valor_veiculo - entrada
    taxa = taxa_juros / 100
    parcela = valor_financiado * (taxa * (1+taxa)**parcelas) / ((1+taxa)**parcelas - 1)
    total_pago = parcela * parcelas
    juros = total_pago - valor_financiado
    return total_pago, juros, parcela

# =========================================
# AULA 02 - INTRODUÇÃO AO PYTHON
# =========================================

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def lista_cidades():
    cidades = ["Paris","Roma","Tokyo","NY","Londres","Berlim","Lisboa","Sydney","Toronto","Rio"]
    for cidade in reversed(cidades):
        print(cidade)

def lista_nomes(nomes):
    for nome in nomes:
        print(nome)

def media_notas(qtd, notas):
    return sum(notas) / qtd

def imprimir_felicidade():
    palavra = "FELICIDADE"
    for i, letra in enumerate(palavra):
        print(f"Posição {i}: {letra}")
    print("Programa finalizado.")

def piramide():
    for i in range(1, 13):
        print("*" * i)

def primeiros_impares(n):
    contador = 0
    i = 1
    while contador < n:
        if i % 2 != 0:
            print(i)
            contador += 1
        i += 1

def multiplicar_por_5(lista):
    return [x * 5 for x in lista]

# =========================================
# AULA 04 - CLASSES EM PYTHON
# =========================================

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def mostrar_nome(self):
        print(self.nome)
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    def imprimir_endereco(self):
        print(self.endereco)

class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    def alterar_editora(self, nova):
        self.editora = nova
    def listar_qtde_paginas(self):
        return self.paginas

class Aluno:
    def __init__(self, nome, ra, notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas
    def mostrar_situacao(self):
        media = sum(self.notas)/len(self.notas)
        if media >= 7:
            return "APROVADO"
        elif media >= 5:
            return "EXAME"
        return "REPROVADO"

class Conta:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
    def imprimir_saldo(self):
        print(f"Saldo: {self.saldo}")

class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def nome_completo(self):
        print(f"{self.nome} {self.sobrenome}")
    def calcular_salario(self):
        print(f"Salário: {self.horas_trabalhadas * self.valor_hora}")
    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def imprimir_raio(self):
        print(self.raio)
    def calcular_area(self):
        return 3.14 * self.raio ** 2
    def calcular_circunferencia(self):
        return 2 * 3.14 * self.raio

class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    def validar_data(self):
        return 1 <= self.dia <= 31 and 1 <= self.mes <= 12
    def anotar_tarefa(self, texto):
        self.anotacao = texto
    def mostrar_anotacao(self):
        print(self.anotacao)

class Triangulo:
    def __init__(self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    def get_maior_lado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.9
        return self.mensalidade

class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivel=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel
    def abastecer(self, litros):
        self.nivel += litros
    def andar(self, km):
        self.nivel -= km / self.consumo
    def verificar_nivel(self):
        return self.nivel
    def calcular_imposto(self):
        return self.valor * 0.035

class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0
    def obter_numero(self):
        return self.numero
    def obter_data_emissao(self):
        return self.data
    def alterar_razao_social(self, nova_razao):
        self.razao_social = nova_razao
    def calcular_valor_total(self):
        self.valor_total = self.valor_produto + self.frete + self.icms + self.ipi
        return self.valor_total
