# range(): gera uma faixa de números

# range() com 1 argumento: gera uma lista de números que vai de zero até argumento menos um (-1)
for i in range(10):
    print(i)

print('----------------------')

# range() com 2 argumentos: gera uma lista de números começando pelo primeiro argumento (inclusive) até o segundo argumento (exclusive) 
for j in range(5, 15):
    print(j)

print('---------------------')

# range() com 3 argumentos:
# 1º limite inferior inclusive;
# 2º limite superior exclusive;
# 3º passo/salto (de quanto em quanto a lista irá contar/andar)
for k in range(1, 22, 3):
    print(k)

print('----------------------')

for n in range(10, 0, -1):
    print(n)