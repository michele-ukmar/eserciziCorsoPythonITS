import numpy as np

matrice = np.zeros((6,3))

for indiceRiga in range (6):
    for indiceColonna in range(3):
        matrice[indiceRiga, indiceColonna] = indiceRiga + indiceColonna
        
print(matrice)
