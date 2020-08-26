import random


isQuit = True


while isQuit == True:

    tärning1 = random.randint(1, 6)
    tärning2 = random.randint(1, 6)
    print(f"Tärning 1 {tärning1}")
    print(f"Tärning 2 {tärning2}")
    if tärning1 == tärning2:
        print(f"du fick två {tärning1}or")

    avsluta = input("Vill du avsluta klicka J")
    avsluta = avsluta.upper()
    if avsluta == "J":
        isQuit = False
