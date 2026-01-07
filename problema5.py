dividendo = float(input("inserisci dividendo"))
divisore = float(input("inserisci divisore"))
quoziente = 0

while dividendo >= divisore:
    dividendo -= divisore
    quoziente += 1
    
print ("quoziente :", quoziente, "resto:", dividendo)