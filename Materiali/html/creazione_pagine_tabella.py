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

# Aggiungi un link a Google al body
link_tag = soup.new_tag("a", href="https://www.google.com")
link_tag.string = "Visita Google"
body_tag.append(link_tag)

# Crea una tabella e aggiungila al body
table_tag = soup.new_tag("table")
body_tag.append(table_tag)

# Aggiungi righe e colonne alla tabella
for i in range(2):
    tr_tag = soup.new_tag("tr")
    table_tag.append(tr_tag)
    for j in range(3):
        td_tag = soup.new_tag("td")
        td_tag.string = f"Riga {i+1}, Colonna {j+1}"
        tr_tag.append(td_tag)

# Stampa il documento HTML
print(soup.prettify())

# Salva il documento HTML
with open("creazione_pagine_tabella.html", "w") as file:
    file.write(str(soup))