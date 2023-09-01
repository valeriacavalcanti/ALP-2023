"""
Escreva um programa para ler 06 números.
Exiba quantos números são iguais ao último valor digitado.
"""

# declarar o contador
qtd = 0

# declarar o vetor
numeros = [0] * 6

# ler os valores e armazenar no vetor
for i in range(6):
    numeros[i] = int(input('Valor: '))

# comparar cada elemento do vetor com o último
for i in range(5):
    if (numeros[i] == numeros[5]):
        qtd = qtd + 1

# exibir a quantidade encontrada
print(qtd)
