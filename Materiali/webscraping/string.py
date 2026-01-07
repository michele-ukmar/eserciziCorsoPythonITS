from bs4 import BeautifulSoup 
import requests 
url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

title_tag = soup.title
title_tag.string
# 'Welcome to Python.org'

print(title_tag.string)
# Welcome to Python.org

head_tag = soup.head
print(head_tag.string)
# None

print(soup.html.string)
# None