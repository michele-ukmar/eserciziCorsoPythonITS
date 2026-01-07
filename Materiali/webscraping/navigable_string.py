from bs4 import BeautifulSoup
soup = BeautifulSoup("<h2 id='message'>Hello, Python!</h2>")

print(soup.string)
# 'Hello, Python!'

print(type(soup.string))
# <class 'bs4.element.NavigableString'>

soup.string.replace_with("Online Learning!")
# 'Hello, Python!'

print(soup.string)
# 'Online Learning!'

print(soup)
# <html><body><h2 id="message">Online Learning!</h2></body></html>