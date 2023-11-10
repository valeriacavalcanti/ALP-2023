st = "Fera 2025 IFPB"

for i in range(len(st)):
    if (st[i] >= 'A') and (st[i] <= 'Z'):
        print(st[i], '- letra maiúscula', ord(st[i]))
    elif (st[i] >= 'a') and (st[i] <= 'z'):
        print(st[i], '- letra minúscula', ord(st[i]))
    elif (st[i] >= '0') and (st[i] <= '9'):
        print(st[i], '- símbolo numérico', ord(st[i]))
    else:
        print(st[i], '- caractere especial', ord(st[i]))
