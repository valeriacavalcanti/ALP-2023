lista = [0] * 8
qtd = 0

while (qtd < 8):
   numero = int(input("Valor: "))

   # verificar se o número está na lista
   
   # partir da hipótese que não existe, ou seja:
   existe = False

   for i in range(qtd):
        if (numero == lista[i]):
            existe = True
            break
 
   if (existe == False):
        lista[qtd] = numero
        print(numero, 'inserido no índice', qtd)
        print(lista)
        qtd = qtd + 1

print(lista)
