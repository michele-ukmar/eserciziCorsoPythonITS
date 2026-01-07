from bs4 import BeautifulSoup

# Crea un nuovo documento HTML vuoto
soup = BeautifulSoup(features="html.parser")

# Crea un tag HTML
html_tag = soup.new_tag("html")

# Crea un tag HEAD e aggiungilo all'HTML
head_tag = soup.new_tag("head")
html_tag.append(head_tag)

# Crea un tag TITLE e aggiungilo all'HEAD
title_tag = soup.new_tag("title")
title_tag.string = "Il mio primo documento HTML"
head_tag.append(title_tag)

# Crea un tag BODY e aggiungilo all'HTML
body_tag = soup.new_tag("body")
html_tag.append(body_tag)

# Crea un tag H1 e aggiungilo al BODY
h1_tag = soup.new_tag("h1")
h1_tag.string = "Benvenuti nel mio primo documento HTML"
body_tag.append(h1_tag)

# Crea un tag P e aggiungilo al BODY
p_tag = soup.new_tag("p")
p_tag.string = "Questa è una pagina HTML creata con Beautiful Soup"
body_tag.append(p_tag)

# Stampa il documento HTML
print(soup.prettify())

# Salva il documento HTML
with open("creazione_pagine.html", "w") as file:
    file.write(str(soup))
