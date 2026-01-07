from bs4 import BeautifulSoup

# Crea un nuovo documento HTML vuoto
soup = BeautifulSoup(features="html.parser")

# Crea un tag HTML e aggiungilo al documento
html_tag = soup.new_tag("html")
soup.append(html_tag)

# Crea un tag HEAD e aggiungilo all'HTML
head_tag = soup.new_tag("head")
soup.html.append(head_tag)

# Aggiungi uno stile CSS personalizzato
style_tag = soup.new_tag("style")
style_tag.string = "p {color: red; font-size: 20px;}"
soup.head.append(style_tag)

# Crea un tag BODY e aggiungilo all'HTML
body_tag = soup.new_tag("body")
# soup.html.append(body_tag)

# Crea un tag P con un testo e aggiungilo al BODY
p_tag = soup.new_tag("p")
p_tag.string = "Questo è un paragrafo"
body_tag.append(p_tag)
soup.html.append(body_tag)
soup.html.replace_with(body_tag)


# Stampa il documento HTML
print(soup.prettify())

# Salva il documento HTML
with open("creazione_pagina_css.html", "w") as file:
    file.write(str(soup))

