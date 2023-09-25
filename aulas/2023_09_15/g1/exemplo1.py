quantidade = 0
lista = [0] * 8
numero = 0

while (quantidade < 8):
    numero = int(input('Número: '))
    # partir da hipótese que o número nao (false) na lista
    tem = False
    # verificar se numero está na lista
    for i in range(quantidade):
        if (lista[i] == numero):
            tem = True
            break
    # verifificar se a hipótese é verdadeira, ou seja,
    # o número nao está na lista
    if (tem == False):
        lista[quantidade] = numero
        print(numero, "armazenado no índice:", quantidade)
        print(lista)
        quantidade = quantidade + 1

# exibir os números armazenados
print(lista)
print(quantidade)
