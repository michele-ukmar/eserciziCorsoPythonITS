from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Tag di prova</b>', 'lxml') 
tag = soup.html

print(tag.name)
#  'html’

tag.name = "Strong"
print(tag)
# <Strong><body><b class="boldest">Tag di prova</b></body></Strong>

print(tag.name)
'Strong'