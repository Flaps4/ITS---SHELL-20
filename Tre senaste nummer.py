nummer_lista = []
summa = 0

while True:
    nummer = int(input("Skriv in nummer"))
    summa = nummer + summa
    print("summa", summa)

    nummer_lista.append(nummer)
    print("Senaste tre nummer", nummer_lista[-3:])

    if number == 0:
        print("Nu avslutas programmet")
        break
