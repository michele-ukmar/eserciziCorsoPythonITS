import pandas as pd

# Crea il primo DataFrame
data1 = {'A': [1, 2],
         'B': [3, 4]}
df1 = pd.DataFrame(data1)

# Crea il secondo DataFrame
data2 = {'A': [5, 6],
         'B': [7, 8]}
df2 = pd.DataFrame(data2)

# Esegui la sottrazione delle due matrici
result = df1 - df2


# Questo codice crea due DataFrame df1 e df2 utilizzando due dizionari e la funzione
#  pd.DataFrame() della libreria pandas. Esegue quindi la sottrazione delle due matrici 
# utilizzando l’operatore -.


import pandas as pd
import numpy as np

# Crea un DataFrame
data = {'A': [1, 2],
        'B': [3, 4]}
df = pd.DataFrame(data)

# Calcola il prodotto matriciale tra il DataFrame e la sua trasposta
matrix_product = np.dot(df, df.T)


# Questo codice crea un DataFrame df utilizzando un dizionario e la funzione pd.DataFrame() della libreria pandas. Calcola quindi il prodotto matriciale tra il DataFrame e la sua trasposta utilizzando la funzione np.dot() della libreria numpy.

# In questo esempio, abbiamo utilizzato la funzione np.dot() della libreria numpy per eseguire un calcolo matriciale sul DataFrame. Questo ci permette di sfruttare la potenza dei calcoli matriciali per analizzare i dati in modo efficiente.


