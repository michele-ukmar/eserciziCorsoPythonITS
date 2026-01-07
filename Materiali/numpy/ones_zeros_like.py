import numpy as np
a = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]],dtype=np.float32)

b = np.zeros_like(a)
print(b)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
b = np.ones_like(a)
print(b)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
b = a.copy()


