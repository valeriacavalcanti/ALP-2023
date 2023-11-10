import random

# declarar matriz A
matrizA = []
for i in range(4):
    matrizA.append([0]*3)

# declarar matriz B
matrizB = []
for i in range(4):
    matrizB.append([0]*3)

# declarar matriz C
matrizC = []
for i in range(4):
    matrizC.append([0]*3)

# preencher a matriz A
for i in range(4):
    for j in range(3):
        #print("Linha {} Coluna {}".format(i, j))
        #matrizA[i][j] = int(input("Valor: "))
        matrizA[i][j] = random.randint(1,5)

# preencher a matriz B
for i in range(4):
    for j in range(3):
        #print("Linha {} Coluna {}".format(i, j))
        #matrizA[i][j] = int(input("Valor: "))
        matrizB[i][j] = random.randint(1,5)

# somar as matrizes A e B
for i in range(4):
    for j in range(3):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

# exibir a matriz A e a matriz B
#print(matrizA)
#print(matrizB)

print("MATRIZ A")
for i in range(len(matrizA)):
    print(matrizA[i])

print("MATRIZ B")
for i in range(len(matrizB)):
    print(matrizB[i])

print("MATRIZ C")
for i in range(len(matrizC)):
    print(matrizC[i])
