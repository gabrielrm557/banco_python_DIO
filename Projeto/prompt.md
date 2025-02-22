Contexto: 
Projeto de um prototipo de um banco contendo funções de saque,deposito, limites, permitindo uma manipulação maior do dinheiro

linguagem utilizada : Python

exemplo : 
            
    '''
            saldo -= saquefloat
                saque = 'R$' + saque + ' '
                registro_saque += saque
                print(f'Você sacou R${saquefloat} seu saldo atual é de R${saldo}')
                saque_diario_limite -= 1 
    '''


desafio do bootcamp de python da dio

requisitos do projeto : 

#sacar,depositas,visualizar extrato

#deposito : valores positivos,armazenado em variavel e exibido no extrato

#saque : maximo 3 por dia,maximo de R$500 por saque,caso não tenha saldo
#exibir uma mensagem informando que não sera possivel sacar o dinheiro
#todos saques exibidos em uma varivel e exibidos na operação extrato

#extrato : listar depositos e saques realizados na conta
#no fim da listagem deve exibir o saldo atual da conta

#formatação tem que ser em R$

REGRAS : 
 - Sempre que citar alguma dependência do projeto, deixa ela como hyperlink para a página oficial daquela dependência
 - Organize as dependências em uma sessão em formato de tabela
 
 - crie uma estrutura do projeto com base na arvore de pastas abaixo, e crie uma sessão para explicitar as técnicas utilizadas
 
    Projeto
    banco py 2.0
    README.md