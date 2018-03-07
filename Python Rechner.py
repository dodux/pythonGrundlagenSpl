print("Taschenrechner (+/-/:/*/**)")

abfrage = input("Wollen sie mit Kommerzahlen rechnen? (y/n)")

if(abfrage == "y"):
  zahl1 = float(input("Erste Zahl:"))
  rechenzeichen = input("Rechenzeichen:")  
  zahl2 = float(input("Zweite Zahl:"))

if(abfrage == "n"):
  zahl1 = int(input("Erste Zahl:"))
  rechenzeichen = input("Rechenzeichen:")
  zahl2 = int(input("Zweite Zahl:"))

if(rechenzeichen == "/"  and zahl2 == 0.0):
  print("Error sie koennen nicht durch 0 dividieren!")
  exit()


if(rechenzeichen == "+"):
  ergebnis =  zahl1 + zahl2
  print(zahl1 , "+" , zahl2, "=" , ergebnis)
  
  
  
if(rechenzeichen == "-"):
  ergebnis =  zahl1 - zahl2
  print(zahl1 , "-" , zahl2, "=" , ergebnis)
  
  
  
if(rechenzeichen == "/"):
  ergebnis =  zahl1 / zahl2
  print(zahl1 , "/" , zahl2, "=" , ergebnis)
  
  
  
if(rechenzeichen == "*"):
  ergebnis =  zahl1 * zahl2
  print(zahl1 , "*" , zahl2, "=" , ergebnis)
  
  
  
if(rechenzeichen == "**"):
  ergebnis =  zahl1 ** zahl2
  print(zahl1 , "**" , zahl2, "=" , ergebnis)
  