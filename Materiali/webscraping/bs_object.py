
from bs4 import BeautifulSoup
soup = BeautifulSoup("<h2 id='message'>Hello, Python!</h2>", 'lxml')

print(type(soup))
# <class 'bs4.BeautifulSoup'>

print(soup.name)
# '[document]'