import numpy as np

# Creiamo un array 3x3
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Creiamo un array di forma incompatibile
b = np.array([10, 20])
print(b)
# [10 20]

# Tentiamo di moltiplicare gli array 
# usando il broadcasting
c = a * b

# Genera un errore di broadcasting
