import time
import numpy as np
start_time = time.time()
my_arr = np.arange(1000000)
end_time = time.time()
total_time = end_time - start_time
print(total_time) # 0.002000093460083008

start_time = time.time()
my_list = list(range(1000000))
end_time = time.time()
total_time = end_time - start_time
print(total_time) # 0.03500008583068848

# compare in scientific notation
# 2.000093460083008e-06
# 3.500008583068848e-05

