Protótipo de Banco

Descrição

Este é um protótipo de banco desenvolvido em Python como parte do desafio do bootcamp de Python da DIO. O projeto permite aos usuários realizar operações financeiras básicas, como:

Depósito de valores

Saque de dinheiro

Controle de limites diários de saque

Registro de transações (extrato)

Tecnologias Utilizadas

Linguagem: Python

Funcionalidades

Saque

O usuário pode realizar saques respeitando o saldo disponível e os limites estabelecidos:

Máximo de 3 saques diários

Valor máximo de R$500 por saque

Caso não haja saldo suficiente, uma mensagem será exibida informando a impossibilidade do saque

Todos os saques serão registrados no extrato

saldo -= saquefloat
saque = 'R$' + saque + ' '
registro_saque += saque
print(f'Você sacou R${saquefloat} seu saldo atual é de R${saldo}')
saque_diario_limite -= 1 

Depósito

Os usuários podem adicionar fundos à sua conta bancária.

Apenas valores positivos são permitidos

O valor é armazenado e exibido no extrato

saldo += depositofloat
registro_deposito += 'R$' + str(depositofloat) + ' '
print(f'Você depositou R${depositofloat} seu saldo atual é de R${saldo}')

Extrato

A funcionalidade de extrato lista todos os depósitos e saques realizados na conta.

No final da listagem, o saldo atual da conta será exibido

print("Extrato bancário")
print(registro_deposito + registro_saque)
print(f"Saldo atual: R${saldo}")

Como Usar

Clone este repositório:

git clone https://github.com/seu-usuario/prototipo-banco.git

Navegue até o diretório do projeto:

cd prototipo-banco

Execute o script em Python:

python main.py

Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Basta abrir um Pull Request neste repositório.
