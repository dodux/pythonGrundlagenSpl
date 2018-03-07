import random

print("Zahlenraten - errate meine Zahl!")

versuche = int(input("Wie viele Versuche moechtest du haben?"))+1

zahlmin = int(input("Kleinste Zahl:"))

zahlmax = int(input("Groeßte Zahl:"))

zufallszahl = random.randint(zahlmin, zahlmax)

for x in range(1,versuche):
  
  zahl = int(input("Wie lautet dein Versuch?"))
  if(zahl == zufallszahl):
    print("Gratuliere! Du hast die Zahl erraten.")
    break
  
  versuche += 1
    
  if(zahl < zufallszahl):
    print("Die gefragte Zahl ist groeßer!")
    
    
  if(zahl > zufallszahl):
    print("Die gefragte Zahl ist kleiner!")
    


if(x == versuche):
    print("Du hast die maximale Anzahl an Versuchen erreicht! Die Zahl war",zuffalszahl)
    exit()