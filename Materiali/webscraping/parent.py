from bs4 import BeautifulSoup 
import requests 
url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

Ttag = soup.title
print(Ttag)
# <title>Welcome to Python.org</title>

print(type(Ttag.string.parent))
# <class 'bs4.element.Tag'>

html_tag = soup.html
print(type(html_tag.parent))
# <class 'bs4.BeautifulSoup'>

print(soup.parent)
# None