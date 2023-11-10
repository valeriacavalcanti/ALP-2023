qt = 0

# declarar o tabuleiro
tabuleiro = []
for i in range(4):
    tabuleiro.append([0] * 6)

# ler a localização das 20 peças
for i in range(6):
    linha = int(input('Linha: '))
    coluna = int (input('Coluna: '))
    if (tabuleiro[linha][coluna] == 0):
        tabuleiro[linha][coluna] = 1
        #qt = qt + 1

for i in range(4):
    for j in range(6):
        if (tabuleiro[i][j] == 1):
            qt = qt + 1

print('Peças inseridas =', qt)

# forma 1
# print(tabuleiro)

# forma 2
#for i in range(4):
#    print(tabuleiro[i])

# forma 3
for i in range(4):
    for j in range(6):
        #print(tabuleiro[i][j], end=' ')
        if (tabuleiro[i][j] == 0):
            print('L ', end='')
        else:
            print('X ', end='')
    print()
