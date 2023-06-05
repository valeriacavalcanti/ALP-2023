soma = 0

for i in range(4):
    num = int(input("Valor {}: ".format(i + 1)))
    soma = soma + num

media = soma / 4

print(soma)
print(media)
