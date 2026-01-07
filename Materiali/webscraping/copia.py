
from bs4 import BeautifulSoup
import copy

markup = "<p>Learn Python and <b>Java</b> and advanced <b>Java</b>! from my WebSite</p>"
soup = BeautifulSoup(markup, "html.parser")
p_copy = copy.copy(soup.p)

print(p_copy)
# <p>Learn Python and <b>Java</b> and advanced <b>Java</b>! from my WebSite</p>

print(soup.p == p_copy)
#  True

print(soup.p is p_copy)
# False

print(p_copy.parent)
# None