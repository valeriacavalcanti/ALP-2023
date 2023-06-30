# SOLUÇÃO 01
import random

menor = 0
maior = 100

sorteio = random.randint(menor,maior)

print(menor, maior)
num = int(input('Valor: '))

while (num != sorteio):
    if (num > sorteio):
        #print('Maior')
        maior = num
    else:
        #print('Menor')
        menor = num

    print(menor, maior)
    num = int(input('Valor: '))

print('saiu')
