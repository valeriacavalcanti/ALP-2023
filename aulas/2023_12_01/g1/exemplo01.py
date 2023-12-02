import funcoes

# PROGRAMA PRINCIPAL

frase = input('Digite a frase: ')

qt_letras = funcoes.letras(frase)
qt_vogais = funcoes.vogais(frase)
qt_palavras = funcoes.palavras_2v(frase)
qt_simbolos = len(frase)

print('Quantidade de letras:', qt_letras)
print('Quantidade de vogais:', qt_vogais)
print('Quantidade de palavras:', qt_palavras)
print('Quantidade de símbolos:', qt_simbolos)

