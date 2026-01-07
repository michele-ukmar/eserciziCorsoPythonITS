import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

# Create a DataFrame with a custom index
df = pd.DataFrame(data, index=['X', 'Y', 'Z'])

# Display the DataFrame
print(df)

#    A  B
# X  1  4
# Y  2  5
# Z  3  6

# Select data using the index
print(df.loc['X'])


# A    1
# B    4
# Name: X, dtype: int64

pd.Index(['X1', 'Y1', 'Z1'])

print(df.loc['X1'])