import numpy as np

# Creiamo un array 3x3
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Creiamo un array con un solo valore
b = np.array([10])
print(b)
# [10]

# Moltiplichiamo gli array usando il broadcasting
c = a * b

print(c)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

