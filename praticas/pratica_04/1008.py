num = input('Número: ')
horas = int(input('Horas: '))
valor = float(input('Valor: '))

salario = horas * valor

print('NUMBER =', num)
print('SALARY = U$', salario)
print('SALARY = U$ {:-10.2f}'.format(salario))
