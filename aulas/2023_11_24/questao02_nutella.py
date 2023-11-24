qt_mai = qt_min = qt_num = qt_esp = 0

texto = input("Texto: ")
for i in range(len(texto)):
    if (texto[i].isupper()):
        qt_mai += 1
    elif (texto[i].islower()):
        qt_min += 1
    elif (texto[i].isdigit()):
        qt_num += 1
    else:
        qt_esp += 1

print('maiusculas:',qt_mai)
print('minusculas:',qt_min)
print('numericos:',qt_num)
print('especiais:',qt_esp)
