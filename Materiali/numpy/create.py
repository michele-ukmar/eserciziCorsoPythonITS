import numpy as np

# Creare una matrice (6, 3)
matrice = np.zeros((6, 3))

# Impostare ogni elemento su rowIndex + columnIndex
for rowIndex in range(6):
    for columnIndex in range(3):
        matrice[rowIndex, columnIndex] = rowIndex + columnIndex

# Stampare la matrice
print(matrice)
# [[0. 1. 2.]
#  [1. 2. 3.]
#  [2. 3. 4.]
#  [3. 4. 5.]
#  [4. 5. 6.]
#  [5. 6. 7.]]