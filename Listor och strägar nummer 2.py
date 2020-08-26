import statistics

temp_lista = []

temp_antal = int(input("Antal mätningar: "))

for i in range(temp_antal):
    temp_värde = float(input())
    temp_lista.append(temp_värde)

    print(len(temp_lista))

##median
median = statistics.median(temp_lista)

print("Median 0: ",median)

median1 = sum(temp_lista) / len(temp_lista)
print("Median 1:", median1 )

##summa
maxvärde = sum(temp_lista)
print("Maxvärde: ",maxvärde)

    

