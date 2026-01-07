import pandas as pd
import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/realwage.xlsx")
df = pd.read_excel(file_dir,sheet_name='foglio prova', header=1, na_values=['NA'])

df =  df[df.isnull().any(axis=1)].head()

df.mean()

print(df.head())