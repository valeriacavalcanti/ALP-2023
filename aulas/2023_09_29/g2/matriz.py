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


# ler os elementos da matriz A
for i in range(4):
    for j in range(3):
        #matrizA[i][j] = int(input("Valor: "))
        matrizA[i][j] = random.randint(1,5)

# ler os elementos da matriz B
for i in range(4):
    for j in range(3):
        #matrizB[i][j] = int(input("Valor: "))
        matrizB[i][j] = random.randint(1,5)

# somar os elementos das matrizes A e B --> armazenar na matriz C
for i in range(4):
    for j in range(3):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

#print(matrizA)
#print(matrizB)
#print(matrizC)

print('Matriz A')
for i in range(4):
    print(matrizA[i])

print('Matriz B')
for i in range(4):
    print(matrizB[i])

print('Matriz C')
for i in range(4):
    print(matrizC[i])
