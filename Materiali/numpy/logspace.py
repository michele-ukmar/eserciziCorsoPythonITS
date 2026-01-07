
import numpy as np

start = 0.
stop = 10.
nPoints = 11
alog = np.logspace(start, stop, nPoints, base=10.0, dtype=None, axis=0)

print(alog)
# [1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05 1.e+06 1.e+07 1.e+08 1.e+09
#  1.e+10]