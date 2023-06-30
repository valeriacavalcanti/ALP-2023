# SOLUÇÃO 02
import random

menor = 0
maior = 100

sorteio = random.randint(menor,maior)

while (True):
    print(menor, maior)
    num = int(input('Valor: '))

    if (num == sorteio):
        break

    if (num > sorteio):
        #print('Maior')
        maior = num
    else:
        #print('Menor')
        menor = num
    
print('saiu')
