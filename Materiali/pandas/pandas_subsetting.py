
import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/realwage.xlsx")
df = pd.read_excel(file_dir,sheet_name='foglio prova', index_col=None, na_values=['NA'], header=1)

print(df[df['Pay period']=='Annual'].describe())

print(df[df['Pay period']=='Hourly'].describe())

# trasformo da orario in annuale
df1 = df.loc[df['Pay period']=='Hourly',:] 
df1['ValueN'] = df1['value'] * 8 * 48 * 5
print(df1['value'] * 8 * 48 * 5)

print(df1['ValueN'].describe())

print(df1['ValueN'].mean())
print(df1.count())

print(df.loc[df['Country']=='Ireland',['Country','value']])