# Definiamo un decoratore che misura il tempo di esecuzione di una funzione
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo impiegato da {func.__name__}: {end_time - start_time} secondi")
        return result
    return wrapper

# Utilizziamo il decoratore per misurare il tempo di esecuzione di una funzione
@timer
def somma(a, b):
    return a + b

print(somma(5, 10))  # Stampa il risultato della somma e il tempo impiegato

# Modifica l'esempio per applicare il decoratore a una funzione che calcoli il fattoriale di un numero
@timer
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)

print(fattoriale(5))  # Stampa il risultato del fattoriale e il tempo impiegato
