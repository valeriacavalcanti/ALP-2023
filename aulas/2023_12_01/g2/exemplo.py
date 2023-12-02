import funcoes

# PROGRAMA PRINCIPAL

frase = input("Digit uma frase: ")

numeros = funcoes.quantidade_numeros(frase)
vogais = funcoes.quantidade_VOGAIS(frase)
palavras = funcoes.quantidade_palavras(frase)
tamanho = len(frase)

print("Quantidade de números:", numeros)
print("Quantidade de vogais maiúsculas:", vogais)
print("Quantidade de palavras:", palavras)
print("Quantidade de símbolos:", tamanho)
