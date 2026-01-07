# Esempio di funzione che legge un file e restituisce le righe in una lista
# questa funzione restituisce una lista di righe

def leggi_file(nome_file):
    file = open(nome_file, "r")
    righe = file.readlines()
    file.close()
    return righe

leggi_file("/Users/lcorsaro/Desktop/proverbio.txt")

# Esempio di funzione che scrive un file a partire da una lista di righe
# questa funzione non restituisce nulla

def scrivi_file(nome_file, righe):
    file = open(nome_file, "w")
    for riga in righe:
        file.write(riga)
    file.close()

def prova():
    print("Ciao")

