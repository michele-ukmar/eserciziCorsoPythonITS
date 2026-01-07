import numpy as np

# create 3 rows, 5 columns
a = np.zeros( (3,5) )
print(a)
# [[ 0.,  0.,  0.,  0.,  0. ],
# [ 0.,  0.,  0.,  0.,  0. ],
# [ 0.,  0.,  0.,  0.,  0. ]  ]
# default type is float64

b = np.ones( (2,3,4), dtype=np.int16 )
print(b)
# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]

#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]

