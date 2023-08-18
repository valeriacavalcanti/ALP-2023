soma = 0
numeros = [0]*8

for i in range(8):
    numeros[i] = int(input("Valor: "))
    #print(numeros)
    soma = soma + numeros[i]

media = soma / 8
print('Média =', media)

for i in range(8):
    if (numeros[i] > media):
        print(i, numeros[i])
