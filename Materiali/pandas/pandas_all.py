import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Verifica se tutti i valori nella colonna 'A' sono minori di 4
print((df['A'] < 4).all())

# Verifica se tutti i valori nel DataFrame sono minori di 10
print((df < 10).all().all())

print((df > 5).all().all())