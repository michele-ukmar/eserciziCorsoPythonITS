import pandas as pd


data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Somma lungo l'asse delle righe (somma ogni colonna)
print(df.sum(axis=0))

# Somma lungo l'asse delle colonne (somma ogni riga)
print(df.sum(axis=1))

# In questo esempio, creiamo un DataFrame di Pandas con tre colonne e tre righe. 
# Quando chiamiamo df.sum(axis=0), otteniamo una Series contenente 
# la somma di ogni colonna del DataFrame. Quando chiamiamo df.sum(axis=1),
#  otteniamo una Series contenente la somma di ogni riga del DataFrame.

print((df > 8).any(axis=1))