limite_saque = 3

def menu():
    print("""
        Bem-vindo ao Banco do Python.
        Por favor, escolha uma das opções abaixo:
        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [4] - Sair
        """)

def banco():
    saldo = 0
    extrato = []
    operacao = [deposito, saque, print_extrato]
    while True:
        menu()
        opcao = int(input("Digite a opção: "))
        if opcao >= 1 and opcao <= 3:
            saldo = operacao[opcao -1](saldo, extrato)
        elif opcao == "4":
            print("Obrigado por utilizar o Banco do Python.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
def deposito(saldo, extrato):
    valor = float(input("Insira o valor que deseja depositar: "))
    if (valor < 0):
        print("Não é possível realizar depósito de valor negativo.")
        return saldo
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo

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
    
banco()