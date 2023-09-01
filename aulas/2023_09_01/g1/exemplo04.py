"""
Escreva um programa para ler 06 números.
Exiba quantos números são iguais ao último valor digitado.
"""

# declarar um contador
qtd = 0

# declarar o vetor
numeros = [0] * 6

# ler os valores
for i in range(6):
    numeros[i] = int(input('Valor: '))

# contar os números que são iguais ao último
for i in range(5):
    if (numeros[i] == numeros[5]):
        qtd = qtd + 1

print(qtd)
