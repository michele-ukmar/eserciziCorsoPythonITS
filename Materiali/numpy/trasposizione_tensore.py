import numpy as np

# Creiamo un tensore 3D
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# Trasponiamo il tensore
b = np.transpose(a, (2, 0, 1))

print("Tensore originale:")
print(a)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

print("Tensore trasposto:")
print(b)
# [[[1 3]
#   [5 7]]
#
#  [[2 4]
#   [6 8]]]

