from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Tag di prova</b>', 'lxml') 
tag = soup.html

print(type(tag))
# <class 'bs4.element.Tag’>
