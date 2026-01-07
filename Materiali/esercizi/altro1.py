# In questo esempio, creiamo una lista di parole casuali e un dizionario vuoto per memorizzare il punteggio del giocatore.
#  Utilizziamo un ciclo di gioco per chiedere al giocatore di indovinare una parola casuale scelta dalla lista. 
# Se il giocatore indovina la parola corretta, gli viene assegnato un punto e chiediamo se vuole continuare a giocare. 
# Se sceglie di uscire, stampiamo il punteggio finale.
# Questo esempio mostra come l'utilizzo delle liste, dizionari e tuple può essere utilizzato per creare un semplice
#  gioco interattivo in Python.

# Creiamo una lista di parole casuali
import random
words = ["ciao", "palla", "gatto", "telefono", "tavolo"]

# Creiamo un dizionario vuoto per memorizzare il punteggio del giocatore
scores = {}

# Creiamo un ciclo di gioco che termina quando il giocatore sceglie di uscire
while True:
    # Scegliamo una parola a caso dalla lista
    word = random.choice(words)
    
    # Chiediamo al giocatore di indovinare la parola
    guess = input("Indovina la parola: ")
    
    # Controlliamo se la parola indovinata è corretta
    if guess == word:
        print("Corretto! La parola era ", word)
        
        # Aggiungiamo il punteggio del giocatore se non è presente nel dizionario
        if not scores.get(guess):
            scores[guess] = 0
        
        # Incrementiamo il punteggio del giocatore
        scores[guess] += 1
        
    else:
        print("Sbagliato! La parola era ", word)
        
    # Chiediamo al giocatore se vuole continuare a giocare
    choice = input("Vuoi continuare a giocare? (s/n)")
    
    # Se il giocatore sceglie di uscire, stampiamo il punteggio e usciamo dal ciclo
    if choice == "n":
        print("Punteggio: ", scores)
        break
