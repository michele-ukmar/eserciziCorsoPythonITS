import numpy as np
import time

startTime = time.time()
myArray = np.arange(1000000)
endTime = time.time()
totalTime = endTime - startTime
print("Tempo di esecuzione: ", totalTime)

startTime = time.time()
mylist = list(range(1000000))
endTime = time.time()
totalTime = endTime - startTime
print("Tempo di esecuzione: ", totalTime)
