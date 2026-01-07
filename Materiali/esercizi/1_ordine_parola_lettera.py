# Esercizio 

# Scrivere un programma per stabilire se una parola viene alfabeticamente prima 
# o dopo di un’altra 

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
i = 0

while i <= min(len(parola1),len(parola2)):
    if parola1[i].lower() < parola2[i].lower():
        print("La prima parola viene prima", parola1, parola2)
        break
    elif parola1[i].lower() > parola2[i].lower():
        print("La seconda parola viene prima:", parola2, parola1)
        break
    i += 1

print("Le parole sono uguali!")