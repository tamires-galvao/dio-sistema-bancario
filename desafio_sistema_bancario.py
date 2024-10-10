# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500
MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Funções
def exibir_menu():
    return input(MENU)

def realizar_deposito(saldo, extrato):
    valor_do_deposito = input("Informe o valor do depósito: ")
    valor_do_deposito = valor_do_deposito.replace(",", ".")
    try:
        valor = float(valor_do_deposito)
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(saldo, extrato, numero_saques):
    valor_do_saque = input("Informe o valor do saque: ")

    valor_do_saque = valor_do_saque.replace(",", ".")
    
    try:
        valor = float(valor_do_saque)
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > LIMITE_SAQUE_VALOR:
        print(f"Operação falhou! Limite de saque é de R$ {LIMITE_SAQUE_VALOR:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Operação falhou! Número máximo de saques ({LIMITE_SAQUES}) excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Operação finalizada. Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()