from bs4 import BeautifulSoup 
import requests 
url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

for string in soup.stripped_strings:
    print(repr(string))

# 'Welcome to Python.org'
# 'Notice:'
# 'While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience.'
# 'Skip to content'
# '▼'
# 'Close'