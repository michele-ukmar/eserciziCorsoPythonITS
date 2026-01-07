import numpy as np

a2 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a2[2, 1]) 
# 8

print(a2[2]) 
# [7, 8, 9]

print(a2[:, 1]) 
# [2, 5, 8]