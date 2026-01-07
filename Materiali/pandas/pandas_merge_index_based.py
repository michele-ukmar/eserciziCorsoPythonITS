import pandas as pd

# Create two simple datasets
data1 = {'A': [1, 2, 3]}
data2 = {'B': [4, 5, 6]}

# Create two DataFrame objects with a common index
df1 = pd.DataFrame(data1, index=['X', 'Y', 'Z'])
df2 = pd.DataFrame(data2, index=['X', 'Y', 'W'])

# Merge the DataFrames on their index
result = pd.merge(df1, df2, left_index=True, right_index=True)

# Display the result
print(result)

#    A  B
# X  1  4
# Y  2  5