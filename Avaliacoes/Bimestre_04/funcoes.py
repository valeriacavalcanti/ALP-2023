import random

def misterio(parametro1, parametro2):
    temp = []
    for i in range(len(parametro1)):
        if ((parametro1[i] % parametro2) == 0):
            temp.append(parametro1[i])
    return temp


def aleatorio(lista, qt):
    lista.clear()
    for i in range(qt):
        lista.append(random.randint(1, 21))


lista = []
aleatorio(lista, 10)
valor = random.randint(1,11)

print(lista)
print(valor)
print(misterio(lista, valor))
