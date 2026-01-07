from bs4 import BeautifulSoup

soup = BeautifulSoup('<p><!-- Everything inside it \
                      is COMMENTS --></p>', 'lxml')
comment = soup.p.string

print(type(comment))
# <class 'bs4.element.Comment'>

print(type(comment))
#  <class 'bs4.element.Comment'>

print(soup.p.prettify())
#  <p>
# <!-- Everything inside it is COMMENTS --> </p>