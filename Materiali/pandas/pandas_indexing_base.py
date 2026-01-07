
import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]}

# Create a DataFrame
df = pd.DataFrame(data)

# Select rows using basic indexing
print(df[1:4][['A','B']])
#    A  B
# 1  2  7
# 2  3  8
# 3  4  9

print(df[1:4].B)
# 1    7
# 2    8
# 3    9

print(df[1:4]['B'])
# 1    7
# 2    8
# 3    9

print(df[1:4][['B']])
#    B
# 1  7
# 2  8
# 3  9