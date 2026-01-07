import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Applica una singola funzione di aggregazione a tutte le colonne
result = df.agg('sum')
print(result)

# Applica diverse funzioni di aggregazione a diverse colonne
result = df.agg({'A': 'sum', 'B': 'mean', 'C': 'min'})
print(result)