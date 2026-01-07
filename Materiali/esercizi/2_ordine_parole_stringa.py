# Esercizio 

# Scrivere un programma per stabilire se una parola viene alfabeticamente prima 
# o dopo di un’altra 

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")

if parola1.lower() < parola2.lower():
    print("La prima parola viene prima", parola1, parola2)
elif parola1.lower() > parola2.lower():
    print("La seconda parola viene prima:", parola2, parola1)
elif parola1.lower() == parola2.lower():
    print("Le parole sono uguali!")