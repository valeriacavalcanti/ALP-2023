"""
Escreva um programa para ler 10 (dez) números.
Ao final, exiba todos os números pares que foram informados.
"""

# declarar o vetor
numeros = [0] * 10

# ler os valores e armazenar no vetor
for i in range(10):
    numeros[i] = int(input("Valor: "))

# verificar cada elemento se é par.
for i in range(10):
    if (numeros[i] % 2 == 0):
        print(numeros[i])
