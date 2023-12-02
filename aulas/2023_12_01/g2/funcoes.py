def quantidade_numeros(texto):
    qt = 0
    for i in range(len(texto)):
        if (texto[i] >= '0') and (texto[i] <= '9'):
            qt = qt + 1

    return qt


def quantidade_VOGAIS(texto):
    qt = 0
    vogais = "AEIOU"
    for i in range(len(texto)):
        if (texto[i] in vogais):
            qt = qt + 1
    return qt


def quantidade_palavras(texto):
    lista = texto.split()
    return len(lista)
