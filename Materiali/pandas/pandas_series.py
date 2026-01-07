import pandas as pd

# creazione di una serie
series1 = pd.Series ([1, 2, 3], index = ['a', 'b','c']) 
print(type(series1))

# creazione di una serie a partire da un dizionario
dict1 = {'a' : 1, 'b' : 2, 'c': 3}
series1 = pd.Series(dict1)

print(series1)
# a    1
# b    2
# c    3
# dtype: int64

print(series1.index)
# Index(['a', 'b', 'c'], dtype='object')

# ottenere il valore di una serie
print(series1.values)
# [1 2 3]

# ottener i valori per indice

print(series1['a'])
# 1
print(series1[['b','a']])

# b    2
# a    1
# dtype: int64

# ottenere l'indice di una serie
print(series1.index )
# Index(['a', 'b', 'c'], dtype='object')

# Attributo Get Name (None è predefinito) 
print(series1.name)
# None
print(series1.index.name)
# None

series1.name = 'serie1'
print(series1.name)
# serie1

series1.index.name = 'serie1.indice'
print(series1.index.name)
# serie1.indice

series1 = pd.Series ([1, 2, 3]) 
series2 = pd.Series ([10, 20, 30]) 
print(series1 + series2)

series1 = pd.Series ([1, 2, 3], index = ['a', 'b','c']) 
series2 = pd.Series ([10, 20, 30], index = ['a', 'd','e']) 
print(series1 + series2)
# a    11.0
# b     NaN
# c     NaN
# d     NaN
# e     NaN
# dtype: int64

series2 = pd.Series ([10, 20, 30], index = ['a', 'b','c']) 
print(series1 + series2)

# a    11
# b    22
# c    33
# dtype: int64

# aggiungere un elemento ad una serie
series1['d'] = 4

series2 = series1.unique()
print(series2)
# [1 2 3]