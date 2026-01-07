# esempio di variabile globale

variabile_globale = 78

def funzione(Y):
    # scopo locale
    global variabile_globale 
    variabile_globale = Y
    print(variabile_globale)


def funzione_prova():
    # scopo locale
    print(variabile_globale)

print(funzione("2"))

funzione_prova()