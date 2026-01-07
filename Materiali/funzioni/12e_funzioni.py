# Crea una funzione che prenda una lista di numeri interi
# e restituisca la somma di tutti gli elementi della lista.

def somma_lista(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

lista_di_numeri = [1, 2, 3, 4, 5]
print(somma_lista(lista_di_numeri)) # output: 15
