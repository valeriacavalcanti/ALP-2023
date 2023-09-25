lista = []

repeticao = False

for i in range(10):
    numero = int(input('Número: '))
    if (numero in lista):
        repeticao = True
    lista.append(numero)

print(lista)
if (repeticao == True):
    print("tem repeticao")
else:
    print("nao tem repeticao")
