import numpy as np
A = np.zeros((3, 3))
B = np.ones((5, 3))
C = np.concatenate((A, B), axis=0)
print(C)
#  [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]


import numpy as np
A = np.zeros((3, 2))
B = np.ones((3, 1))
C = np.concatenate((A, B), axis=1)
print(C)
# [[0. 0. 1.]
#  [0. 0. 1.]
#  [0. 0. 1.]]

