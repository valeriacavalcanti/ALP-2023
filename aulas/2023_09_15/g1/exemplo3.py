lista = []

repeticao = False

for i in range(10):
    numero = int(input('Número: '))
    if (numero in lista):
        repeticao = True
    lista.append(numero)

if (repeticao == False):
    print("Nao tem repeticao")
else:
    print("Tem repeticao")

print(lista)
