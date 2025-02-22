#sacar,depositas,visualizar extrato

#deposito : valores positivos,armazenado em variavel e exibido no extrato

#saque : maximo 3 por dia,maximo de R$500 por saque,caso não tenha saldo
#exibir uma mensagem informando que não sera possivel sacar o dinheiro
#todos saques exibidos em uma varivel e exibidos na operação extrato

#extrato : listar depositos e saques realizados na conta
#no fim da listagem deve exibir o saldo atual da conta

#formatação tem que ser em R$


def menu():
    print(' Menu banco ABC \n')
    print(' 1 - Sacar ')
    print(' 2 - Deposito ')
    print(' 3 - Extrato ')
    print(' 4 - parar ')

SAQUE_VEZ_DIARIO_LIMITE = 500
saque_diario_limite = 3
registro_deposito = ''
registro_saque = ''
saldo = 1000
deposito = 0


menu()
operacao = str(input(' Escreva o nome de qual operação deseja realizar \n'))
operacao = operacao.lower()
while operacao != 'parar':
    if operacao == 'sacar':
        if saque_diario_limite >= 0:
            saque = input('Quanto deseja sacar? ')
            saquefloat = float(saque)
            if saque_diario_limite == 0:
                print(' Você so pode sacar 3 vezes ao dia ')
                operacao = 'a'
                continue     
            elif saquefloat > SAQUE_VEZ_DIARIO_LIMITE:
                print('Você so pode sacar R$500 por dia ')
                continue
            elif saquefloat > saldo:
                print('Você não possui este valor para sacar ')
                continue
            else:
                saldo -= saquefloat
                saque = 'R$' + saque + ' '
                registro_saque += saque
                print(f'Você sacou R${saquefloat} seu saldo atual é de R${saldo}')
                saque_diario_limite -= 1 
        operacao = 'a'
    elif operacao == 'deposito':
        deposito = input('Digite a quantia que quer depositar: ')
        dep_int = float(deposito)
        saldo += dep_int
        deposito = 'R$' + deposito + ' '
        registro_deposito += deposito
        print(registro_deposito)
        operacao = 'a'
    elif operacao == 'extrato':
        print(f'esses foram todos os depositos realizados na sua conta {registro_deposito} ')
        print(f'esses foram todos os saques realizados na sua conta {registro_saque} ')
        print(f'o seu saldo atual é de R${saldo}')
        operacao = 'a'
    elif operacao == 'a':
        menu()
        operacao = str(input(' Escreva o nome de qual operação deseja realizar \n'))
        operacao = operacao.lower()
        continue
    else:
        print('ops parece que você digitou algo errado')
        menu()
        operacao = str(input(' Escreva o nome de qual operação deseja realizar \n'))
        operacao = operacao.lower()


