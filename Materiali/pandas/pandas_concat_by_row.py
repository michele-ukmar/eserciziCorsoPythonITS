import pandas as pd

# Create two simple datasets
data1 = {'A': [1, 2, 3],
         'B': [4, 5, 6]}
data2 = {'A': [1, 2, 4],
         'C': [7, 8, 9]}

# Create two DataFrame objects
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the DataFrames on column 'A' default INNER JOIN
result = pd.merge(df1, df2, on='A')

# Display the result
print(result)

#    A  B  C
# 0  1  4  7
# 1  2  5  8