import re

# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500
AGENCIA = "0001"
MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[cc] Criar Conta Corrente
[lu] Listar Usuários
[lc] Listar Contas
[iu] Inativar Usuário
[q] Sair

=> """

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Funções de apoio
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return cpf

# Criar usuário
def criar_usuario():
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
    cpf = input("Informe o CPF (somente números): ")
    cpf = validar_cpf(cpf)
    if not cpf:
        print("CPF inválido!")
        return

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário cadastrado com esse CPF.")
            return

    endereco = input("Informe o endereço (Logradouro, numero, bairro, cidade/sigla estado): ")
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print(f"Usuário {nome} criado com sucesso!")

# Criar conta corrente
def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário: ")
    cpf = validar_cpf(cpf)
    if not cpf:
        print("CPF inválido!")
        return

    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    contas.append({'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario})
    print(f"Conta corrente {numero_conta} criada para o usuário {usuario['nome']}.")

# Inativar usuário
def inativar_usuario():
    cpf = input("Informe o CPF do usuário a ser inativado: ")
    cpf = validar_cpf(cpf)
    if not cpf:
        print("CPF inválido!")
        return

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            print(f"Usuário {usuario['nome']} inativado com sucesso.")
            return

    print("Usuário não encontrado.")

# Listar contas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Usuário: {usuario['nome']} (CPF: {usuario['cpf']})")

# Funções principais do sistema
def realizar_saque(*, saldo, extrato, numero_saques):
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

def realizar_deposito(saldo, extrato, /):
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

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Fluxo principal
def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(MENU)

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "cc":
            criar_conta_corrente()

        elif opcao == "lu":
            for usuario in usuarios:
                print(usuario)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "iu":
            inativar_usuario()

        elif opcao == "q":
            print("Operação finalizada. Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
