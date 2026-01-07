
from bs4 import BeautifulSoup
markup = "<p>Learn Python and <b>Java</b> and advanced <b>Java</b>! from MyWebSite</p>"
# <p>
#  Learn Python and
#  <b>
#   Java
#  </b>
#  and advanced
#  <b>
#   Java
#  </b>
#  ! from MyWebSite
# </p>

soup = BeautifulSoup(markup, "html.parser") 
print(soup.prettify())
first_b, second_b = soup.find_all('b')
print(first_b == second_b)
# True
print(first_b.previous_element)
# Learn Python and 
print(second_b.previous_element)
#  and advanced 
print(first_b.previous_element == second_b.previous_element) 
# False