

from UFS02.decoratore_definizione import funzione_decoratore

@funzione_decoratore
def mia_funzione2():
    print("Hello World!")

mia_funzione2()
# output:

# ... codice da eseguire prima di funzione_parametro ...
# hello world!
# ... codice da eseguire dopo di funzione_parametro ...