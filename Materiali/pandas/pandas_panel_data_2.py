import pandas as pd
# Create a simple dataset in long format
data = {'ID': [1, 1, 1, 2, 2, 2],
        'Year': [2000, 2001, 2002, 2000, 2001, 2002],
        'Income': [1000, 2000, 3000, 4000, 5000, 6000]}
# Create a DataFrame
df = pd.DataFrame(data)
print(df)
#    ID  Year  Income
# 0   1  2000    1000
# 1   1  2001    2000
# 2   1  2002    3000
# 3   2  2000    4000
# 4   2  2001    5000
# 5   2  2002    6000
# Set the index to be the ID and Year columns
df = df.set_index(['ID', 'Year'])
# Unstack the DataFrame to convert it to wide format
df = df.unstack(level='Year')
# Display the result
print(df)
#     Income            
# Year   2000  2001  2002
# ID                     
# 1      1000  2000  3000
# 2      4000  5000  6000