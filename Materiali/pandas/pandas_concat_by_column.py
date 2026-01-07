import pandas as pd
# Create two simple datasets
data1 = {'A': [1, 2],
         'B': [3, 4],
         'C': [5, 6]}
data2 = {'A': [5, 6],
         'B': [7, 8]}

# Create two DataFrame objects
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenate the DataFrames vertically
result = pd.concat([df1, df2])

# Display the result
print(result)

#    A  B    C
# 0  1  3  5.0
# 1  2  4  6.0
# 0  5  7  NaN
# 1  6  8  NaN

import pandas as pd

# Create two simple datasets
data1 = {'A': [1, 2]}
data2 = {'B': [3, 4]}

# Create two DataFrame objects
df1 = pd.DataFrame(data1, index=['X', 'Y'])
df2 = pd.DataFrame(data2, index=['X', 'Z'])

# Concatenate the DataFrames horizontally
result = pd.concat([df1, df2], axis=1)

# Display the result
print(result)

#      A    B
# X  1.0  3.0
# Y  2.0  NaN
# Z  NaN  4.0