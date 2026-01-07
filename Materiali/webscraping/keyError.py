from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p>Questo è un paragrafo</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
tag = soup.find('a')

print(tag['href'])

# Traceback (most recent call last):
#   File "example.py", line 11, in <module>
#     tag['href']
# KeyError: 'href'
