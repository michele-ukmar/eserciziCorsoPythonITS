import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

# Create a DataFrame with a custom index
df = pd.DataFrame(data, index=['X', 'Y', 'Z'])

# Select data using loc
print(df.loc['X'])

# A    1
# B    4
# Name: X, dtype: int64