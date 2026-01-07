import os
import pandas as pd

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/realwage.csv")
# open a csv file usign relative path
df = pd.read_csv(file_dir)

print(df.head())
print(df.columns)

file_dir = os.path.join(current_dir + "/realwage.xlsx")
df2 = pd.read_excel(file_dir,sheet_name='foglio prova', index_col=None, na_values=['NA'])
print(df2.head())
print(df2.columns)

df3 = pd.read_excel(file_dir,sheet_name='foglio prova', header=1, na_values=['NA'])
print(df3.head())
print(df3.columns)

print(type(df3))
print(type(df3.Time))

print(type(df3.Time[1]))
df.Time = pd.to_datetime(df.Time)
print(type(df.Time[1]))
print(df3.head())

print(type(df3.value[1]))
df.value = pd.to_numeric(df.value)
print(type(df.value[1]))
print(df3.head())

print(df3.head(3))

print(df3.head(-13))

# df3 = pd.read_stata('myfile.dta')
# df4 = pd.read_sas('myfile.sas7bdat')
# df5 = pd.read_hdf('myfile.h5','df')


print(type(df.Time[1]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# controlla il tipo di dato di una serie
print(df.Time.dtypes)
# datetime64[ns]

# controlla il tipo di dato di una serie
print(df['Time'].dtype)
# datetime64[ns]

# controlla il tipo di dato di tutte le colonne del dataframe
print(df.dtypes)
# Time          datetime64[ns]
# Unnamed: 0             int64
# Country               object
# Series                object
# Pay period            object
# value                float64
# dtype: object

print(df.size)

print(df.shape)

print(df.ndim)
    
print(df.axes)

print(df.describe())

print(df.sample(10))

print(df.head(50).mean())

print(df.head(10).std())


print(df.std())
print(df.min())
print(df.max())
print(df.median())
print(df.head(10).describe())
print(df.count())