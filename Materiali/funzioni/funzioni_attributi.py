
def funzione_prova():
        print("Hello World")

print(funzione_prova.__name__)
#stampa il valore di un singolo attributo

print(dir(funzione_prova))
# stampa gli attributi della funzione


def funzione_prova(what):
        """Questa funzione stampa Hello World"""
        funzione_prova.used += 1 
        print(what)




print(funzione_prova.__doc__)

funzione_prova.used = 0
funzione_prova("Hello World")
funzione_prova("Hello World")
print(funzione_prova.used)
