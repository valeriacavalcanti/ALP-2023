matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

for i in range(3):
    for j in range(3):
        print(i,j)
        #matriz[i][j] = 'X'

#matriz[0][1] = 'X'
#matriz[1][1] = 'X'
#matriz[2][1] = 'X'

#print(matriz)

for i in range(3):
    print(matriz[i])

# rodadas
for i in range(4):
    # perguntar X
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    matriz[linha][coluna] = 'X'

    for j in range(3):
        print(matriz[j])

    # perguntar O
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    matriz[linha][coluna] = 'O'

    for j in range(3):
        print(matriz[j])
