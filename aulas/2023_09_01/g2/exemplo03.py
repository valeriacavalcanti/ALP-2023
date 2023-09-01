"""
Escreva um programa para ler 06 (seis) números.
Exiba os números lidos do último até o primeiro,
ou seja, na ordem inversa que foram lidos.
"""

# declarar o vetor
numeros = [0] * 6

# ler o valores e armazenar no vetor
for i in range(6):
    numeros[i] = int(input('valor: '))


# exibir na ordem inversa da leitura
for i in range(6,-1,-1):
    print(numeros[i])
