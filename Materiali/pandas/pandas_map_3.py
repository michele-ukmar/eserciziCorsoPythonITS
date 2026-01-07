import pandas as pd

# Create a simple dataset
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Define a mapping function
def square(x):
    return x ** 2

# Map values in column 'A' using the mapping function
df['A'] = df['A'].map(square)

# Display the result
print(df)