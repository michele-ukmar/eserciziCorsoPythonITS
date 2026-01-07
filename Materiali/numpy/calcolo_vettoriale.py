import pandas as pd
import numpy as np

# Crea un DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Calcola il prodotto scalare tra le colonne A e B
dot_product = np.dot(df['A'], df['B'])

# Calcola il prodotto vettoriale tra le colonne A e B
cross_product = np.cross(df['A'], df['B'])

# Questo codice crea un DataFrame df utilizzando un dizionario e la funzione pd.DataFrame() 
# della libreria pandas. Calcola quindi il prodotto scalare tra le colonne A e B utilizzando 
# la funzione np.dot() della libreria numpy, e il prodotto vettoriale tra le colonne A e B 
# utilizzando la funzione np.cross() della libreria numpy.

# In questo esempio, abbiamo utilizzato le funzioni della libreria numpy per eseguire calcoli 
# vettoriali sulle colonne del DataFrame. Questo ci permette di sfruttare la potenza dei
#  calcoli vettoriali per analizzare i dati in modo efficiente.