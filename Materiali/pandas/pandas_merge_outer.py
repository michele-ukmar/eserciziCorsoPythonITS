# Questo codice crea due DataFrame df1 e df2 utilizzando due dizionari e la funzione pd.DataFrame() della libreria pandas.
#  Imposta quindi gli indici dei due DataFrame utilizzando il metodo set_index() e specificando le colonne da utilizzare come indici (id1 e id2).
# Infine, esegue un join dei due DataFrame utilizzando il metodo join() e specificando il tipo di join (inner).

# In questo esempio, il join viene eseguito utilizzando gli indici dei due DataFrame. Poiché abbiamo impostato gli
#  indici utilizzando le colonne id1 e id2, il join viene eseguito su queste due colonne. Il risultato è un
#  DataFrame che contiene solo le righe in cui i valori di id1 e id2 sono presenti in entrambi i DataFrame originali.

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

#    id     nome   città   età genere
# 0   1    Alice    Roma  25.0      F
# 1   2      Bob  Milano  30.0      M
# 2   3  Charlie  Napoli   NaN    NaN
# 3   4      NaN     NaN  35.0      F

df_merged = pd.merge(df1, df2, on='id', how='inner')
print(df_merged)

#    id   nome   città  età genere
# 0   1  Alice    Roma   25      F
# 1   2    Bob  Milano   30      M
