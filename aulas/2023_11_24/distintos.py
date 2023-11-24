memoria_simbolos = []
memoria_palavras = []

original = input('Texto: ')
texto = original.upper()
palavras = texto.split()

# identificar os diferentes simbolos
for i in range(len(texto)):
    if (texto[i] not in memoria_simbolos):
        memoria_simbolos.append(texto[i])

# identificar as diferentes palavras no texto
for i in range(len(palavras)):
    if (palavras[i] not in memoria_palavras):
        memoria_palavras.append(palavras[i])

print(memoria_simbolos)
print(memoria_palavras)
