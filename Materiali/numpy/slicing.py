import numpy as np
a = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])

print(a[1])
# [4 5 6]
print(a[1,:])
# [4 5 6]
print(a[1,1:])
# [5 6]
print(a[:1,1:])
# [[2 3]]

arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]

arr_slice = arr[5:8]
print(arr_slice)
# [5 6 7]
arr_slice[1] = 12345
print(arr)                      
# [    0     1     2     3     4     5 12345     7     8     9]
arr_slice[:] = 64
print(arr)                      
# [ 0  1  2  3  4 64 64 64  8  9]
