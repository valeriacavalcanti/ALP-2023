vogais = 'AEIOUaeiou'
qt = 0

texto = input("Texto: ")

for i in range(len(texto)):
    if (texto[i] in vogais):
        qt += 1

print('vogais:', qt)
