import numpy as np

# Creiamo un array a 2 dimensioni
a = np.array([[1, 2], [3, 4]])

# Creiamo un array a 3 dimensioni
b = np.array([[[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(b)
# [[[ 5  6]
#   [ 7  8]]
#   [[ 9 10]
#   [11 12]]]

# Applichiamo il broadcasting tra a e b
c = a + b

print(c)
# [[[ 6  8]
#   [10 12]]
#   [[10 12]
#   [14 16]]]
