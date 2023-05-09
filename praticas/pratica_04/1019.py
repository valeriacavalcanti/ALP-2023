tempo = int(input('Tempo: '))

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60

print(horas, minutos, segundos, sep=':')
