from bs4 import BeautifulSoup 
import requests 
url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

for sibling in soup.head.next_siblings: 
    print(repr(sibling))
# \n
# <body> .... </body>

for sibling in soup.body.previous_siblings: 
    print(repr(sibling))
# \n
# <head> .... </head>