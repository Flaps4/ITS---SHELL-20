import re
AdressCheck = input("Email")
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', AdressCheck)

if match == None:
    print('Felaktig email')
    raise ValueError('Dålig syntax')
