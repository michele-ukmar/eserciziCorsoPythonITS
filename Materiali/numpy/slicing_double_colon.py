import numpy as np

# Creiamo un array 1D di numeri interi
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing: selezioniamo gli elementi 
# dall'indice 0 fino alla fine
print(a[::])

# Slicing: selezioniamo gli elementi 
# dall'indice 0 fino alla fine con un passo di 2
print(a[::2])

# Slicing: selezioniamo gli elementi
#  dall'indice 1 fino alla fine con un passo di 2
print(a[1::2])

# Slicing: selezioniamo gli elementi
#  dall'indice -3 fino alla fine
print(a[-3::])

# Creiamo un array 2D di numeri interi
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing: selezioniamo tutte le righe e
#  le colonne dall'indice 0 fino alla fine
print(b[::, ::])

# Slicing: selezioniamo tutte le righe e 
# le colonne dall'indice 0 fino alla fine con un passo di 2
print(b[::2, ::2])

# Slicing: selezioniamo le prime due 
# righe e le prime due colonne
print(b[:2, :2])

# Slicing: selezioniamo tutte le righe e
#  le colonne dalla fine all'inizio con un passo di 3
print(b[::, ::-3])
# [[3]
#  [6]
#  [9]]

print(b[::, ::3])
# [[1]
#  [4]
#  [7]]