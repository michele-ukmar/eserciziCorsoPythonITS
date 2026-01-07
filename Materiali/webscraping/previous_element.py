from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>Titolo della pagina</title>
    </head>
  <body>
    <p>Primo paragrafo</p>
    <p>Secondo paragrafo</p>
    <div>
      <p>Terzo paragrafo</p>
    </div>
  </body>
</html>
"""

# ---------------------------------------- tag element
# <p>
#  Secondo paragrafo
# </p>

# ---------------------------------------- previous element
# None
# ---------------------------------------- previous sibling


# Primo paragrafo


soup = BeautifulSoup(html, 'html.parser')
# Ottiene il secondo paragrafo
second_paragraph = soup.find_all('p')[1]

print('-' * 40, "tag element")
print(second_paragraph.prettify())

# Utilizza il metodo .previous_element per ottenere il primo elemento precedente al paragrafo
previous_element = second_paragraph.previous_element

print('-' * 40, "previous element")
# Stampa il tag dell'elemento precedente
print(previous_element.name)

print('-' * 40, "previous sibling")
# Itera sui fratelli precedenti del secondo paragrafo
for sibling in second_paragraph.previous_siblings:
    if hasattr(sibling, 'string'):
        print(sibling.string)
