menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

>> """

saldo = 0.0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo, extrato):

    while True:
        valor_deposito = float(input("\nDigite o valor do seu deposito: "))
        if valor_deposito > 0:     
            saldo += valor_deposito
            extrato += f"\nO valor de R${valor_deposito:.2f} foi depositado na sua conta."
            print(f"O valor R${valor_deposito:.2f} foi depositado na sua conta.\n")
            return saldo, extrato
        else:
            print("Digite um valor valido! O valor não pode ser negativo ou igual a 0.")

def saque(saldo, extrato, numero_saques):

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

def extrato_conta(saldo, extrato):

    print("Extrato das movimentações da conta.")
    print(extrato)
    print(f"\nO saldo atual da sua conta é de R${saldo}")
    return True


while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Deposito")
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == 2:
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingido. Tente novamente Amanhã.")

        elif saldo == 0:
            print("Você não tem saldo suficiente para efetuar um saque, deposite algum valor primeiro!")

        else:
            print("Saque")
            saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques)
        

    elif opcao == 3:
        if saldo == 0 and numero_saques == 0:
            print("Não foram realizadas movimentações. Não é possivel exibir um extrato da sua conta.")
        else:
            print("\n------------------------------Extrato------------------------------\n")
            extrato_conta(saldo, extrato)
            print("\n-------------------------------------------------------------------\n")
            

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")
    
print("\nObrigado por usar os nossos serviços, tenha um ótimo dia!")
