import numpy as np
# Scrivi un programma python:
# Creare una matrice (6, 3)
a = np.ones((6, 3), dtype=np.float16)
# Impostare ogni elemento su rowIndex + columnIndex
for i in range(6):
    for j in range(3):
        a[i, j] = i + j

# Stampare la matrice
print(a)