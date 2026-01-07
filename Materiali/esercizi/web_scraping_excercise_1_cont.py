import os
import pandas as pd

local_file = os.path.join(os.path.dirname(__file__),"web_scraping_esercizio_1.csv")
df = pd.read_csv(local_file)

print(df.describe())
