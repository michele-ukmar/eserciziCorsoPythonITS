from bs4 import BeautifulSoup 
import requests 
url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

link = soup.a
print(link)
# <a href="#content" title="Skip to content">Skip to content</a>

for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# div
# nav
# div
# div
# body
# html
# [document]