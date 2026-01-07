
import pandas as pd

# Crea il primo DataFrame
data1 = {'id': [1, 2, 3],
         'nome': ['Alice', 'Bob', 'Charlie'],
         'città': ['Roma', 'Milano', 'Napoli']}
df1 = pd.DataFrame(data1)

# Crea il secondo DataFrame
data2 = {'id': [1, 2, 4],
         'età': [25, 30, 35],
         'genere': ['F', 'M', 'F']}
df2 = pd.DataFrame(data2)

# Esegui un join dei due DataFrame
df_merged = pd.merge(df1, df2, on='id', how='outer')

print(df_merged)


# Calcola la media dell'età per genere
mean_age_by_gender = df_merged.groupby('genere')['età'].mean()

# Aggiungi una colonna con la media dell'età per genere
df_merged['età_media_per_genere'] = df_merged['genere'].map(mean_age_by_gender)

print(df_merged)


