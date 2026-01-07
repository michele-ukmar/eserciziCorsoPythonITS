import numpy as np

a = np.zeros((3,3))
b = np.ones((3,3))
c = np.concatenate((a,b), axis=0)
print(c)

c = np.concatenate((a,b), axis=1)
print(c)