from bs4 import BeautifulSoup 
import requests 

url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

print(soup.title) 
# <title>Welcome to Python.org</title>


for link in soup.find_all('a'): 
    print(link.get('href')) 

# #content
# #python-network
# /
# https://www.python.org/psf/
# https://docs.python.org
# https://pypi.org/
# /jobs/
# /community-landing/
# #top
# /