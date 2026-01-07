import pandas as pd

dict1 = {'state': ['Ohio', 'CA'], 'year': [2000, 2010]} 

df1 = pd.DataFrame(dict1) 
# columns are placed in sorted order 
print(df1)

df1 = pd.DataFrame(dict1, index = ['row1', 'row2'])
# specifying index 
print(df1)

df1 = pd.DataFrame(dict1, columns = ['year', 'state']) 
# columns are placed in your given order 
print(df1)


print(df1['state'])

print(df1.state)

print(df1.state[0])
print(df1.state[1])

dict1 = {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row1': 3, 'row2': 4}} 

df1 = pd.DataFrame(dict1) 
print(dict1)

dict1 = {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row3': 3, 'row3': 4}} 
df1 = pd.DataFrame(dict1) 
print(dict1)

dict1 = {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row3': 3, 'row4': 4}} 
df1 = pd.DataFrame(dict1) 
print(dict1)


dict1 = {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row1': 3, 'row2': 4}} 
print(df1.columns)
print(df1.index)

print(df1.columns.name)
print(df1.index.name)

print(df1.values)

print(df1.col1["row2"])
