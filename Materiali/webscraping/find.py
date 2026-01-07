from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250" 
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

print(soup.find_all('title',limit=1))
# [<title>IMDb Top 250 - IMDb</title>] 

print(soup.find('title'))
# <title>IMDb Top 250 - IMDb</title>

print(soup.find_all('h2'))
# []

print(soup.find('h2'))
# None