lista = []

while (len(lista) < 8):
    numero = int(input('Número: '))
    if (numero not in lista):
        lista.append(numero)

print(lista)
print(len(lista))
