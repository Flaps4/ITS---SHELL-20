mailAdress = input("Email here --> ")
pos = mailAdress.find("@")

if mailAdress.find("@") == -1:
    print("Something is wrong")
    raise ValueError("FAFerror go back do right")

pos = mailAdress.rfind(".")
mailLen = len(mailAdress)
charsdot = mailLen - pos - 1
if charsdot == 2 or charsdot == 3:
    print("Working")
else:
    raise ValueError("Fel antal tecken efter mail")
