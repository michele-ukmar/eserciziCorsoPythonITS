# Crea una funzione che prenda in input una stringa 
# e restituisca una nuova stringa 
# in cui le vocali sono sostituite dal carattere "-".

def sostituisci_vocali(testo):
    vocali = "aeiouAEIOU"
    for vocale in vocali:
        testo = testo.replace(vocale, "-")
    return testo

stringa_di_testo = "Questo è un esempio di stringa"
print(sostituisci_vocali(stringa_di_testo)) 
# output: "Q--st- è -n -s-mp-- d- str-ng-"
