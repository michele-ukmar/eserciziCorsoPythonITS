import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a mapping dictionary
mapping = {1: 'X', 2: 'Y', 3: 'Z'}

# Map values in column 'A' using the mapping dictionary
df['A'] = df['A'].map(mapping)

# Display the result
print(df)
