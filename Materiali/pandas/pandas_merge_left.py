import pandas as pd
data1 = {'A': [1, 2, 3],
         'B': [4, 5, 6]}
data2 = {'A': [1, 2, 4],
         'C': [7, 8, 9]}

# Create two DataFrame objects
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on column 'A'
result = pd.merge(df1, df2, on='A', how='left')

# Display the result
print(result)

#    A  B    C
# 0  1  4  7.0
# 1  2  5  8.0
# 2  3  6  NaN