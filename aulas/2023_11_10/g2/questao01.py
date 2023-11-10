qt_acima_17 = 0
soma = 0
idades = [0] * 10
acima_media = []

# ler a idade de cada integrante desse grupo
for i in range(10):
    idades[i] = int(input('Idade: '))

# Exibir a idade de todos os integrantes
for i in range(10):
    print('no índice',i,'tem a idade',idades[i])

# Exibir a média da idade do grupo
for i in range(len(idades)):
    soma = soma + idades[i]

media = soma / 10
print('Média =', media)

# Calcular e exibir quantas pessoas possuem maior idade (idade acima de 17 anos)
for i in range(10):
    if (idades[i] > 17):
        qt_acima_17 = qt_acima_17 + 1
        # qt_acima_17 += 1

print('Quantidade acima de 17 =', qt_acima_17)

# Exibir a idade de cada integrante que possuir idade acima da média do grupo.
for i in range(10):
    if (idades[i] > media):
        #print(idades[i])
        acima_media.append(idades[i])

print(acima_media)
        
