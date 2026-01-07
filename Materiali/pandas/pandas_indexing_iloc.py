import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Select data using iloc
print(df.iloc[0])
# A    1
# B    4
# Name: 0, dtype: int64

#Select righe in base al loro indice:
print(df.iloc[10:20,[0, 3, 4, 5]])

# Exception has occurred: IndexError
# positional indexers are out-of-bounds
#   File "pandas_indexing_iloc.py", line 14, in <module>
#     print(df.iloc[10:20,[0, 3, 4, 5]])
# IndexError: positional indexers are out-of-bounds
