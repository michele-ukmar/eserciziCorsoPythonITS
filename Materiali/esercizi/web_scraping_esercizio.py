
from bs4 import BeautifulSoup
import requests
url="https://www.ebay.it/sch/i.html?_nkw=iphone" 
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')


s-item__price