import numpy as np

a1 = np.array([1, 2, 3, 4])
print(a1)  # [1, 2, 3, 4]
print(a1[0]) # 1
print(a1[2]) # 3

arr = np.arange(10)
print(arr)          # [0 1 2 3 4 5 6 7 8 9]
print(arr[5])     #5
print(arr[5:8]) #[5 6 7]
arr[5:8] = 12
print(arr)      #[ 0 1 2 3 4 12 12 12 8 9]

arr = np.arange(10)
print(arr)          # [0 1 2 3 4 5 6 7 8 9]
arr_slice = arr[5:8]
print(arr_slice)            # [5 6 7]
arr_slice[1] = 12345
print(arr)                      # [    0     1     2     3     4     5 12345     7     8     9]
arr_slice[:] = 64
print(arr)                      # [ 0  1  2  3  4 64 64 64  8  9]
