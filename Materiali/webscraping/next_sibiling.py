from bs4 import BeautifulSoup
h_s ="<a><b>Hello Pyhton</b><c><strong>the simplest coding language</strong></c></a>" 
sibling_soup = BeautifulSoup(h_s, 'html.parser')

print(sibling_soup.b.next_sibling)
# <c><strong>the simplest coding language</strong></c>

print(sibling_soup.b.previous_sibling)
# None

print(sibling_soup.c.previous_sibling)
# <b>Hello Pyhton</b>

print(sibling_soup.c.next_sibling)
# None

print(sibling_soup.b.string)
# Hello Pyhton

print(sibling_soup.b.string.next_sibling)
# None