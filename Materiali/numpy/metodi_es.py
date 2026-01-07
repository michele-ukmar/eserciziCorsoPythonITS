import numpy
a = numpy.array([[1,2,3],
          [4,5,6],
          [7,8,9]])

print(a.tolist())
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

b = a.copy()
print(b is a)
# False
print(b == a)
# [[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

b.fill(3)
print(b)
# [[3 3 3]
#  [3 3 3]
#  [3 3 3]]