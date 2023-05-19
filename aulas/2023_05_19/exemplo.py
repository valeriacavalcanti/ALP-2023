nota = int(input("Digite sua nota: "))

if ((nota >= 0) and (nota <= 100)):
    print("Válida")
    print("Parabéns")
    if (nota >= 70):
        print("passou")
    else:
        print("Não passou")
else:
    print("Não é válida")
    print("Sinto muito!")
