from bs4 import BeautifulSoup
markup = "<p>I will display &#x00A3;</p>"
Bsoup = BeautifulSoup(markup)
print(Bsoup.p)
# <p>I will display £</p>
print(Bsoup.p.string)
# 'I will display £'

