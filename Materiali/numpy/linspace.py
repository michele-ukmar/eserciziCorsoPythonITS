import numpy as np

start = 0.
stop = 2.5
nPoints = 10
inclusive = True

a = np.linspace(start, stop, nPoints, inclusive)
	# array of evenly spaced floats
	# begins with start
	# ends with stop
	# can include/exclude stop   True/False

# Useful to make “range” of floats
print(a)
# [0. 0.27777778 0.55555556 0.83333333 1.11111111 1.38888889
#  1.66666667 1.94444444 2.22222222 2.5       ]