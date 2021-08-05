# Função é um trecho de código que tem um nome e pode receber informação externas para fazer seu trabalho. Opcionalmente, uma função pode também produzir um valor de resultado.
# Uma função é definida apenas uma vez e pode ser utilizada (chamada) várias vezes, evitando repetições de código.
# Existem funções já providas pela linguagem, como, por exemplo, len(), range() e sort(), e podemos definir também nossas próprias funções.

# Os termos que aparecem entre parÊnteses  são chamados parâmetros ou argumentos
def imc(peso, altura):
    # Trecho entre aspas triplas são m tipo especial de comentário chamado DOCSTRING, e serve para documentas o propósito de uma função ou classe
    '''
        Função que calcula o índicede Massa Corpóres (IMC)
    '''
    return peso / altura ** 2 # peso dividido por altura ao quadrado

# float(): converte o valor informado em um número com casas decimais (floating point)
p = float(input('Informe o peso da pessoa: '))
a = float(input('Informe a altura da pessoa: '))

# fazendo uma chamada a função imc()
resultado = imc(p, a)

print(f'O IMC calculado é: {resultado}')