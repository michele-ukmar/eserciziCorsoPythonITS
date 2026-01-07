from bs4 import BeautifulSoup 
import requests 

url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

head_tag = soup.head

print(len(head_tag.contents))
# 40

print(len(list(head_tag.children)))
# 40

print(len(list(head_tag.descendants)))
# 105