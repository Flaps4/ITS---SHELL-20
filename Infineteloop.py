lista_nummer = []

tal1 = 0

while True:

    mata = int(input())
    tal1 = tal1 + mata
    lista_nummer.append(mata)


    print("du matade in,", mata)
    print ("summan av alla tal är", tal1)
    print("dina senaste tal var", lista_nummer[-3:])

    if mata == 0:
        print("Du kommer nu stänga ner programmet")
        print("Vänligen tryck ner valfri tangent")
        wait = input()
        break
 ### Hjälp Med Nummer 5