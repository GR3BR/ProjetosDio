menu = """

[0] Cadastrar Cliente
[1] Cadastrar Conta
[2] Depositar
[3] Sacar
[4] Extrato
[5] Sair

>> """

saldo = 0.0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

lista_clientes = {}
numero_da_conta = 0
lista_contas = {}


def criar_cliente(lista_clientes):
    CPF = input("Digite o CPF para o novo cadastro: ")
    if not CPF in lista_clientes:
        nome = input("Digite o seu nome: ")
        data_nascimento = input("Digite a data do seu nascimento(Dia/Mês/Ano): ")
        print("\nInformações de endereço\n")
        logradouro = input("Digite o nome da sua rua: ")
        numero_casa = input("Digite o número da sua casa: ")
        bairro = input("Digite o bairro da sua casa: ")
        cidade = input("Digite a sua cidade: ")
        estado = input("Digite a sigla do estado da sua cidade: ")
        endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"        
        lista_clientes.update({ CPF : {"nome": nome, "data_nascimento" : data_nascimento, "endereco" : endereco }})
        print(lista_clientes[CPF])
        return(lista_clientes, CPF)
    
    else:
        print("CPF já cadastrado, tente novamente com um novo CPF")
        return(lista_clientes)
        
def criar_conta(lista_contas, lista_clientes, numero_da_conta):
    while True:
        usuario_logado = input("Digite o CPF do cliente a ter uma conta cadastrada: ")
        if usuario_logado in lista_clientes:
            numero_da_conta += 1
            lista_contas.update({ numero_da_conta : {"numero_agencia" : "0001", "usuario" : usuario_logado}})
            print(f"Conta {numero_da_conta} criada na agencia 0001 para o usuario de CPF {usuario_logado}")
            return lista_contas, numero_da_conta
        else:
            print("Digite o CPF de um cliente valido.")


def deposito(saldo, extrato, /):

    while True:
        valor_deposito = float(input("\nDigite o valor do seu deposito: "))
        if valor_deposito > 0:     
            saldo += valor_deposito
            extrato += f"\nO valor de R${valor_deposito:.2f} foi depositado na sua conta."
            print(f"O valor R${valor_deposito:.2f} foi depositado na sua conta.\n")
            return saldo, extrato
        else:
            print("Digite um valor valido! O valor não pode ser negativo ou igual a 0.")

def saque(*, saldo, extrato, numero_saques):

    while True:
        valor_saque = float(input("\nDigite o valor do saque a ser efetuado(Limitado a 500 reais por saque): "))
        if valor_saque <= saldo and valor_saque <= 500 and valor_saque > 0:
            saldo -= valor_saque
            extrato += f"\nO valor de R${valor_saque:.2f} foi sacado na sua conta."
            numero_saques += 1
            print(f"\nO valor R${valor_saque:.2f} foi sacado na sua conta.\n")
            return saldo, extrato, numero_saques
        else:
            print("Digite um valor de saque valido! O valor não pode ser maior do que o seu saldo ou maior que 500 reais.")

def extrato_conta(saldo,/ , *, extrato):

    print("Extrato das movimentações da conta.")
    print(extrato)
    print(f"\nO saldo atual da sua conta é de R${saldo}")
    return True


while True:

    opcao = int(input(menu))

    if opcao == 0:
        print("Cadastrar novo cliente")
        lista_clientes, usuario_logado = criar_cliente(lista_clientes)
        
    elif opcao == 1:
        if  lista_clientes == {}:
            print("Faça o cadastro de um cliente para poder cadastrar uma conta.")
            continue
        else:
            print("Cadastrar nova conta")
            lista_contas, numero_da_conta = criar_conta(lista_contas, lista_clientes, numero_da_conta)
            print(lista_contas)

    elif opcao == 2:
        print("Deposito")
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == 3:
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingido. Tente novamente Amanhã.")

        elif saldo == 0:
            print("Você não tem saldo suficiente para efetuar um saque, deposite algum valor primeiro!")

        else:
            print("Saque")
            saldo, extrato, numero_saques = saque(saldo = saldo, extrato = extrato, numero_saques = numero_saques)
        

    elif opcao == 4:
        if saldo == 0 and numero_saques == 0:
            print("Não foram realizadas movimentações. Não é possivel exibir um extrato da sua conta.")
        else:
            print("\n------------------------------Extrato------------------------------\n")
            extrato_conta(saldo, extrato = extrato)
            print("\n-------------------------------------------------------------------\n")
            

    elif opcao == 5:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")
    
print("\nObrigado por usar os nossos serviços, tenha um ótimo dia!")
