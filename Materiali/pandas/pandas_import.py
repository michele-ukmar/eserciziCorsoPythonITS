import pandas as pd
# read the data from the CSV file tab separated
data = pd.read_csv('~/Documents/Dati_Lavoro/alzheimer/raw/GSE153712/GSE153712_normalized_average_betas.txt', sep='\t')
data.head()