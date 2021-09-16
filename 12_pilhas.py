# Palíndrono: é um texto que, quando lido de trás para frente,
# mantém o mesmo conteúdo (desprezando acentos e espaçamento)
#texto = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"
texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha = []

# Percurso do palíndromo em ordem inversa, colocando cada letra na lista
for letra in texto:
    pilha.append(letra) # append() sempre acrescenta por ÚLTIMO

#pilha.insert(10,'y')
#pilha.insert(19, 'g')
#pilha.insert(6, 'ç')

print(pilha)

inverso = ""

# Remove de elementos em posição que não são a final 
# del pilha[11] # remove a posição 11
# del pilha[21] # remove a posição 21
# del pilha[8]
# del pilha[25]

# Retira cada letra da lista, de trás para frente, e coloca no inverso
while len(pilha) > 0:
    inverso += pilha.pop() # pop() retira sempre o ÚLTIMO elemento

print(inverso)

# Pilha
# A pilha é um tipo abstrato de dados (TAD) que permite a entrada e a saída
# de dados apenas na sua extremidade final. Como consequência, ela segue a 
# regra LIFO (last in, first out - último a entrar, primeiro a sair), e tem
# acesso limitado aos seus elementos.
# 