
import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/realwage.xlsx")
df = pd.read_excel(file_dir,sheet_name='foglio prova', index_col=None, na_values=['NA'], header=1)

# sort by Country e value
df.sort_values(by=['Country','value'], inplace=True)
print(df.head(10))

df_sorted = df.sort_values( by =['Country','value'], ascending = [False, False])
print(df_sorted.head(10))

