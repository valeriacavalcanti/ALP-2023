matriz = [['']*3,['']*3,['']*3]

for i in range(3):
    for j in range(3):
        matriz[i][j] = ' '
        #print(i,j)


for i in range(4):
    # ler o jogador X
    linha = int(input('Linha: '))
    coluna = int(input("Coluna: "))
    matriz[linha][coluna] = 'X'

    # ler o jogador O
    linha = int(input('Linha: '))
    coluna = int(input("Coluna: "))
    matriz[linha][coluna] = 'O'

    # exibir a matriz
    for i in range(3):
        print(matriz[i])
