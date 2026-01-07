import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
# [1 2 3 4 5 6]
a = a.reshape(3,2)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]
a = a.reshape(2,-1)
print(a)
# [[1 2 3]
#  [4 5 6]]
a = a.ravel()
print(a)
# [1 2 3 4 5 6]


c = np.arange(24)
d = c.reshape(6,4)
print(d)
print(d.reshape(2,-1))
print(ssd.reshape(2))