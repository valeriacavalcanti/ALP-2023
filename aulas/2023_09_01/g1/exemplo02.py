"""
Programa para ler 4 números.
"""

# declarar o vetor, com tamanho 4
numeros = [0] * 4

print("Minha lista")
print(numeros)

# percorrer os índices do vetor para armazenar os valores.
for i in range(4):
    numeros[i] = int(input('Valor: '))
    print(numeros)
