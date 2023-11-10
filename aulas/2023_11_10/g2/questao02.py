qt = 0

# declarar a matriz 4 x 6
tabuleiro = []
for i in range(4):
    tabuleiro.append([0] * 6)

# ler a posição de 20 peças
for i in range(6):
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if (tabuleiro[linha][coluna] == 0):
        tabuleiro[linha][coluna] = 1

# percorrer a matriz procurando valor 1 (tem peça)
for i in range(4):
    for j in range(6):
        if (tabuleiro[i][j] == 1):
            qt = qt + 1
            # qt += 1

print(qt,'peças inseridas com sucesso')

# exibir o tabuleiro
# print(tabuleiro)

#for i in range(4):
#    print(tabuleiro[i])

for i in range(4):
    print('- ', end='')
    for j in range(6):
        if (tabuleiro[i][j] == 0):
            print('L', end=' ')
        else:
            print('X', end=' ')
    print()

        
