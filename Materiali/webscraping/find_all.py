from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250" 
# config agent
headers = {'User-Agent': 'Mozilla/5.0'}
# richiedi la pagina
content = requests.get(url, headers=headers)
# crea un oggetto BeautifulSoup
soup = BeautifulSoup(content.text, 'html.parser')

print(soup.find('title'))
# <title>Top 250 Movies - IMDb</title>

# Estriamo il titolo principale
for heading in soup.find_all('h1'): print(heading.text)
#  IMDb Top 250 Movies

# estraiamo i sotto titoli
for heading in soup.find_all('h3'): print(heading.text)
# IMDb Charts
# You Have Seen
#  IMDb Charts
# Top Rated Movies by Genre
# Recently Viewed