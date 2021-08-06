# Importar o valor da constante pi
#math é o nome da biblioteca onde se encontra
from math import pi
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

print('---------------------------------------')

def area_forma(base, altura, forma = "R"):
    '''
    Função qe calcula a área de uma das seguintes formas geométricas: retângulo, triângulo ou elipse
    Parâmetro forma:
    'R' == retângulo (parâmetro opcional com valor padrão)
    'T' == triângulo
    'E' == elipse
    '''
    area = 0
    if forma =='R': # Retangulo
        area = base * altura
    elif forma == 'T': # Triângulo
        area = base * altura / 2
    elif forma == 'E': # Elipse
        area = (base / 2) * (altura / 2) * pi
    return area

print(f"Retângulo 7.5x 11 {area_forma(7.5, 11, 'R')}")
print(f"Triângulo 8x 12 {area_forma(8, 12, 'T')}")
print(f"Círculo 15x 15: {area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5x 9.5 {area_forma(9.5, 9.5)}")

        