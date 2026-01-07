
# Esempio di utilizzo della funzione filter()
# filter(funzione_condizione, sequenza)

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def condizione(numero):
    return numero % 2 == 0

numeri_pari = list(filter(condizione, numeri))

print(numeri_pari) # Output: [2, 4, 6, 8, 10]
