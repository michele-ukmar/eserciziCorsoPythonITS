from bs4 import BeautifulSoup 
import requests 

url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

head_tag = soup.head
print(type(head_tag))
# <class 'bs4.element.Tag'>

print(type(head_tag.contents))
# <class 'list'>

print(len(head_tag.contents))
# 40

Ttag = head_tag.contents[1]
print(Ttag)
#  Google tag (gtag.js) 

print(type(Ttag))

# print(Ttag.contents)
# self.__class__.__name__, attr))
# AttributeError: 'NavigableString' object has no attribute 'contents'

print(soup.contents[1].name)
# 'html'

for child in head_tag.children:
    print(child) 