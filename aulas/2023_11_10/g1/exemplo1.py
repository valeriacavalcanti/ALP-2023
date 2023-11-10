st = 'IFPB 2023 eita!'

for i in range(len(st)):
    if (st[i] >= 'A') and (st[i] <= 'Z'):
        print(st[i], ord(st[i]), '- letra maiúscula')
    elif (st[i] >= 'a') and (st[i] <= 'z'):
        print(st[i], ord(st[i]), '- letra minúscula')
    elif (st[i] >= '0') and (st[i] <= '9'):
        print(st[i], ord(st[i]), '- símbolo numérico')
    else:
        print(st[i], ord(st[i]), '- caractere especial')


print(st)
