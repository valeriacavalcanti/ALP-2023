soma = 0
numeros = [0]*10

for i in range(10):
    numeros[i] = int(input('Digite um valor: '))
    #print(numeros)
    soma = soma + numeros[i]

media = soma / 10

print('Média =', media)

for i in range(10):
    if (numeros[i] > media):
        print(i, '-', numeros[i])
