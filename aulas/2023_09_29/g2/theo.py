import random

def criarMatriz(matriz):
    for i in range(4):
        matriz.append([0]*3)

def imprimirMatriz(matriz):
    print('Elementos da Matriz')
    for i in range(4):
        print(matriz[i])

# declarar as matrizes
matrizA = []
matrizB = []
matrizC = []

criarMatriz(matrizA)
criarMatriz(matrizB)
criarMatriz(matrizC)

imprimirMatriz(matrizA)
imprimirMatriz(matrizB)
imprimirMatriz(matrizC)
