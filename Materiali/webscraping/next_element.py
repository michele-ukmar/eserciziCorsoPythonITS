from bs4 import BeautifulSoup

html = '<html><body><p>First paragraph.</p><p>Second paragraph.</p><div><p>Third paragraph.</p></div></body></html>'

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

# Ottiene il primo elemento dopo l'apertura del tag <html>
first_element = soup.html.next_element

# Itera sui nodi successivi, stampando il testo di ogni 
# elemento che ha un attributo "string"
for element in first_element.next_elements:
    if hasattr(element, 'string'):
        print(element.string)

print('-' * 40)

# Ottiene il primo paragrafo
first_paragraph = soup.find('p')

# Itera sui fratelli successivi del primo paragrafo
for sibling in first_paragraph.next_siblings:
    if hasattr(sibling, 'string'):
        print(sibling.string)
