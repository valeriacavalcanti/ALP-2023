valor = int(input('Valor: '))

c100 = valor // 100
c50 = (valor % 100) // 50
c20 = ((valor % 100) % 50) // 20
c10 = (((valor % 100) % 50) % 20) // 10
c5 = ((((valor % 100) % 50) % 20) % 10) // 5
c2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
c1 = (((((valor % 100) % 50) % 20) % 10) % 5) % 2

print()
