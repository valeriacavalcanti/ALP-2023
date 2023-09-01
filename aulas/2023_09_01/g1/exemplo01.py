"""
Escreva um programa para ler 10 (dez) números.
Ao final, exiba todos os números pares que foram informados.
"""

# declarar o vetor, com tamanho 10
numeros = [0] * 10

# percorrer os índices do vetor para armazenar os valores.
for i in range(10):
    numeros[i] = int(input('Valor: '))

# percorrer os índides do vetor para testar os valores armazenados.
for i in range(10):
    if (numeros[i] % 2 == 0):
        print(numeros[i])
