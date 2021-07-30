# print(): exibe informação
print("Olá, Mundo!")

# input(): permite entrada de informações
nome = input('Qual é o seu nome? ')

print(f"Olá, {nome}!")

idade = int(input('Informe a sua idade: '))

# int() converte o que foi informado no input() de texto para número inteiro
if idade >= 18:
    print('Você já pode beber.')
    print('Você já pode tirar habilitação')
else:
    print('Você não pode beber')
    print('Você não pode tirar habilitação')