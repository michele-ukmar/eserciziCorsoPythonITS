
# definisco la funzione da decorare
from decoratore_definizione import funzione_decoratore


def mia_funzione():
    print("Hello World!")

# decoro la funzione
mia_funzione = funzione_decoratore(mia_funzione)

# chiamo la funzione decorata
mia_funzione()

# ... codice da eseguire prima di funzione_parametro ...
# Hello World!
# ... codice da eseguire dopo di funzione_parametro ...
