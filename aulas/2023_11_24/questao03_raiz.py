vogais = 0

texto = input("Texto: ")

for i in range(len(texto)):
    if (texto[i] >= 'a') and (texto[i] <= 'z'):
        codigo = ord(texto[i])
        codigo -= 32
        simbolo = chr(codigo)
        if (simbolo == 'A') or(simbolo == 'E') or (simbolo == 'I') or (simbolo == 'O') or (simbolo == 'U'):
            vogais += 1

print('vogais:',vogais)
