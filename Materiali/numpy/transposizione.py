
import numpy as np
a = np.arange(10).reshape(5,2) 
print(a)
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]

a = a.T 
print(a)
# [[0 2 4 6 8]
#  [1 3 5 7 9]]

a = a.transpose((1,0)) 
print(a)
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]