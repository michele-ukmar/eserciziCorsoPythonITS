htlm="""<html>
  <head>
    <title>Titolo della pagina</title>
  </head>
  <body>
    <h1>Intestazione della pagina</h1>
    <p class="intro">Questo è un paragrafo di introduzione.</p>
    <p>Questo è un altro paragrafo.</p>
  </body>
</html>"""

# Supponiamo di eseguire il seguente codice Python che cerca di estrarre 
# l'attributo id dal tag <p>:

import os
from bs4 import BeautifulSoup

file_full_path = __file__
file_dir = os.path.dirname(file_full_path)
html_file_path = os.path.join(file_dir, 'python.html')
# Parsing del documento HTML
html_doc = open(html_file_path)
soup = BeautifulSoup(html_doc, 'html.parser')

# Seleziona il tag <p> e cerca l'attributo 'id'
paragrafo = soup.find('p')
id_paragrafo = paragrafo['id']

# Exception has occurred: KeyError
# 'id'
#   File ".../attributeError.py", line 27, in <module>
#     id_paragrafo = paragrafo['id']
# KeyError: 'id'

# Se il tag <p> non ha l'attributo id, il codice precedente genererà 
# un'eccezione AttributeError, poiché stiamo cercando di accedere a un 
# attributo che non esiste. In tal caso, il messaggio di errore 
# sarà qualcosa di simile a:

# Questo errore indica che il tag <p> non ha l'attributo id, quindi non può essere 
# acceduto con la sintassi tag['id']. Per evitare questo errore, 
# è possibile utilizzare il metodo get() di Beautiful Soup per 
# accedere all'attributo in modo sicuro e gestire il caso in cui
# l'attributo non esiste:# 

id_paragrafo = paragrafo.get('id')
if id_paragrafo is not None:
    # L'attributo 'id' esiste, esegui qualche azione
    pass