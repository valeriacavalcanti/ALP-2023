soma = 0
qt_acima_17 = 0
idades = [0] * 10
acima_media = []

# ler as idades das pessoas
for i in range(10):
    idades[i] = int(input("Idade: "))

# exibir a idade de cada pessoa
for i in range(10):
    print('no índice', i, 'tem idade', idades[i])

# calcular a média
for i in range(10):
    soma = soma + idades[i]
    # soma += idades[i]

media = soma / 10
print('Média =', media)

# calcular quantas pessoas possuem idade acima de 17
for i in range(10):
    if (idades[i] > 17):
        qt_acima_17 = qt_acima_17 + 1
        # qt_acima_17 += 1

print('Quantidade acima de 17 =', qt_acima_17)

# exibir a idade de cada pessoa que possuir idade acima da média do grupo
for i in range(10):
    if (idades[i] > media):
        #print(idades[i], 'é acima da média do grupo')
        acima_media.append(idades[i])
print(acima_media)
        
