import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)

file_dir = os.path.join(current_dir + "/realwage.csv")
# df2 = pd.read_excel(file_dir,sheet_name='foglio prova', 
#                     index_col=None, na_values=['NA'],
#                     header=1, dtype={'Country':str} )

df2 = pd.read_csv(file_dir, sep=',')

print(df2.head())
print(df2.columns)
print(df2.dtypes)

df2_country = df2.groupby('Country')
print(df2_country.mean())

# raggruppa per due colonne
print(df2.groupby(['Country','Series'])[['value']].mean())

print(df2.groupby(['Country'], sort=False)[['value']].mean())


df_sub = df2[ df2['value'] > 12000 ]
print(df_sub)

df_f = df2[ df2['Country'] == 'Germany']
print(df_f)

df_f = df2[(df2['Country'] == 'Germany') & (df2['value'] > 12000)]

print(df_f)

