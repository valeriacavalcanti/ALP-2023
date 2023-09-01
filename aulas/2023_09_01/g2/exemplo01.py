"""
Programa para ler 4 números.
"""

# Declarar o vetor
numeros = [0] * 6

# imprimir o vetor
print(numeros)

# Ler os 6 valores e armazenar no vetor
for i in range(6):
    numeros[i] = int(input("Valor: "))
    print(numeros)
