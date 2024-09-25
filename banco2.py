import datetime

limite_saque = 3

def log_transacao(func):
    def safe(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.datetime.now()}: {func.__name__}")
        return resultado
    return safe

def menu():
    print("""
        Bem-vindo ao Banco do Python.
        Por favor, escolha uma das opções abaixo:
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [4] - Cadastrar Cliente
        [5] - Cadastrar Conta Bancária
        [6] - Exibir Clintes
        [7] - Sair
        """)

def banco():
    saldo = 0
    extrato = []
    clientes = []
    contas = []
    operacao = [deposito, saque, print_extrato]
    while True:
        menu()
        opcao = int(input("Digite a opção: "))
        if opcao >= 1 and opcao <= 3:
            saldo = operacao[opcao -1](saldo, extrato)
        elif opcao == 4:
            cadastra_clientes(clientes)
        elif opcao == 5:
            cadastra_conta(contas)
        elif opcao == 6:
            exibir_clientes(clientes)
        elif opcao == 7:
            print("Obrigado por utilizar o Banco do Python.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
    
@log_transacao
def deposito(saldo, extrato):
    valor = float(input("Insira o valor que deseja depositar: "))
    if (valor < 0):
        print("Não é possível realizar depósito de valor negativo.")
        return saldo
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo

@log_transacao
def saque(saldo, extrato):
    global limite_saque
    valor = float(input("Insira o valor que deseja sacar: "))
    if (valor > saldo):
        print("Não é possível realizar o saque. Saldo insuficiente.")
        return saldo
    elif (valor < 0 and limite_saque > 0) :
        saldo += valor
    elif (valor > 0 and limite_saque > 0):
        saldo -= valor
    elif (limite_saque == 0):
        print("Limite de saque diário excedido.")
        return saldo
    extrato.append(f"Saque: - R$ {valor:.2f}")
    limite_saque -= 1
    print(f"limite: {limite_saque}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo

@log_transacao
def print_extrato(saldo, extrato):
    print("############################################")
    print()
    print("Extrato Bancário:")
    print()
    if not extrato:
        print("Nenhuma operação foi realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print()
    print(f"Saldo: R$ {saldo:.2f}")
    print()
    print("############################################")
    
def cadastra_clientes(clientes):
    usuario = input("Insira o nome do cliente: ")
    clientes.append(usuario)
    
def cadastra_conta(contas):
    conta = input("Insira conta: ")
    contas.append(conta)
    
def exibir_clientes(clientes):
        print("############################################")
        print()
        print("Clientes: ")
        for cliente in clientes:
            print(cliente)
        print()
        print("############################################")
    
banco()