import pandas as pd
import os

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/titanic3.xls")
# open a csv file usign relative path
df = pd.read_excel(file_dir, header=0, na_values=['NA'])

df.info()
print(df.shape)
print(df.head())
print(df.columns)

sv = df.groupby(['sex','survived'])[['survived']].count()
sv_tot = df.groupby(['sex','survived'])[['survived']].sum()



print(sv_tot/sv)