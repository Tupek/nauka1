# <liczba rzutów kostką>d/D<liczba ścianek na kostce>+/-<modyfikator wyniku>

import re

def check_dice(str):
    return re.match(r"\d*[d]\d[\+|\-]?\d?", str, re.I) !=None

print(check_dice("9D7+g fghh"), False)  # <---nie dziala

print( check_dice("9d7+10"), True )
print( check_dice("9s7+10"), False )
print( check_dice("9D7+10 abcdefghijk"), True )
print( check_dice("9d-h"), False )
print( check_dice("D6"), True )
print( check_dice("6D3-10"), True )

# to jedno nie działa, do poprawki