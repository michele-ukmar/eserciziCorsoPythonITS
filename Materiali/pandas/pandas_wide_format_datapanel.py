import pandas as pd

# Crea un data panel in formato wide
data = {'id': [1, 2],
        1: [10, 40],
        2: [20, 50],
        3: [30, 60]}
df = pd.DataFrame(data)

# Esegui qualche operazione sui dati in formato wide
df['media'] = df[[1, 2, 3]].mean(axis=1)

# Trasforma i dati in formato long
df_long = pd.melt(df, id_vars=['id', 'media'], value_vars=[1, 2, 3], var_name='tempo', value_name='valore')


#Questo codice crea un data panel in formato wide df utilizzando 
# un dizionario e la funzione pd.DataFrame() della libreria pandas. 
# Esegue quindi qualche operazione sui dati in formato wide (in questo caso, 
# calcola la media di ogni riga). Infine, trasforma i dati in formato long 
# utilizzando la funzione pd.melt().