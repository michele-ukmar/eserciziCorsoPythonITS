
import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/realwage.xlsx")
df = pd.read_excel(file_dir,sheet_name='foglio prova', index_col=None, na_values=['NA'], header=1)

#seleziona la Colonna value:
print(df['value'])
#seleziona la Colonna value e country:
print(df[['Country','value']])
print(df[10:20])

print(df[10:20][['Country','value']])
print(df.loc[10:20,['Country','value']])
print(df.iloc[10:21,[5,2]])

