
import pandas as pd

# Crea il primo DataFrame
data1 = {'id1': [1, 2, 3],
         'id2': ['a', 'b', 'c'],
         'nome': ['Alice', 'Bob', 'Charlie']}
df1 = pd.DataFrame(data1)

# Crea il secondo DataFrame
data2 = {'id1': [1, 2, 4],
         'id2': ['a', 'b', 'd'],
         'età': [25, 30, 35]}
df2 = pd.DataFrame(data2)

# Imposta gli indici dei due DataFrame
df1 = df1.set_index(['id1', 'id2'])
df2 = df2.set_index(['id1', 'id2'])

# Esegui un join dei due DataFrame
df_merged = df1.join(df2, how='inner')

print(df_merged)

#           nome  età
# id1 id2            
# 1   a    Alice   25
# 2   b      Bob   30


# altro esempio di join 

import pandas as pd

# Create two simple datasets
data1 = {'A': [1, 2, 3]}
data2 = {'B': [4, 5, 6]}

# Create two DataFrame objects with a common index
df1 = pd.DataFrame(data1, index=['X', 'Y', 'Z'])
df2 = pd.DataFrame(data2, index=['X', 'Y', 'W'])

# Join the DataFrames on their index
result = df1.join(df2)

# Display the result
print(result)

#    A    B
# X  1  4.0
# Y  2  5.0
# Z  3  NaN