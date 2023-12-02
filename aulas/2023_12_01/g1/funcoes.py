# FUNÇÃO

def letras(texto):
    qt = 0
    for i in range(len(texto)):
        if (texto[i].isalpha()):
            qt += 1
    return qt


def vogais(texto):
    qt = 0
    for i in range(len(texto)):
        if (texto[i] in 'AEIOUaeiou'):
            qt += 1
    return qt

def palavras_1v(texto):
    qt = 0
    for i in range(len(texto)):
        if (texto[i] == ' '):
            qt += 1
    return qt + 1


def palavras_2v(texto):
    lista = texto.split()
    return len(lista)

            
