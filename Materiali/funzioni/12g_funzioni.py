# Crea una funzione che prenda in input due 
# liste di numeri interi e restituisca una nuova 
# lista contenente 
# solo gli elementi che si trovano in entrambe le liste. 

def intersezione_liste(lista1, lista2):
    intersezione = []
    for numero in lista1:
        if numero in lista2 and numero not in intersezione:
            intersezione.append(numero)
    return intersezione

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(intersezione_liste(lista1, lista2)) # output: [4, 5]
