
"""
Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara
alla talen i en array. Loopa igenom arrayen och ta fram det tal som är störst. Skriv
tillbaka resultatet på skärmen för användaren 

-----------------------------------------
list1 = [0]

num = int(input("Enter number of elements in list"))

for i in range(1, num + 1):
    elements = int(input("Enter elements"))
    list1.append(elements)

print(max(list1))
"""







"""
Skapa ett program där användaren får mata in två tal. Låt sedan programmet skriva ut alla
tal som finns mellan dessa två tal på skärmen.
"""
list = [0]

num = int(input("Antal platser i listan 0 - 10: "))

for i in range(1, num + 1):
    elm = int(input())

    list.append(elm)
    print("Det största talet är ")

    print(len(list))
    print(max(list))



