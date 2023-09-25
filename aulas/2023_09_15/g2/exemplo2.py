lista = []

while (len(lista) < 8):
   numero = int(input("Valor: "))

   if (numero not in lista):
        lista.append(numero)

print(lista)
