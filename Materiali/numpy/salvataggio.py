
import numpy as np

a = np.array([1, 2, 3])

np.savez('data.npz', a=a)
data = np.load('data.npz')
a = data['a']
