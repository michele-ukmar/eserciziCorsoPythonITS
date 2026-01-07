
import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Verifica se ci sono valori maggiori di 8 nella colonna C
print((df['C'] > 8).any())

# Il codice specificato restituisce un valore booleano che indica se qualsiasi 
# nella colonna 'C' del DataFrame 'df' è true o no.
print(df['C'].any())

print((df > 8).any())

# Verifica se ci sono valori maggiori di 8 in tutto il DataFrame
print((df > 8).any().any())