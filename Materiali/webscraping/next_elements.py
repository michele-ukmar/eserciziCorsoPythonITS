from bs4 import BeautifulSoup

# Definisci un documento HTML di esempio
html_doc = """
<html>
<head>
	<title>Titolo della pagina</title>
</head>
<body>
	<h1>Intestazione della pagina</h1>
	<p>Questo è un paragrafo.</p>
	<div>
		<p>Questo è un paragrafo in un div.</p>
		<ul>
			<li>Primo elemento della lista</li>
			<li>Secondo elemento della lista</li>
			<li>Terzo elemento della lista</li>
		</ul>
	</div>
	<p>Questo è un altro paragrafo.</p>
</body>
</html>
"""

# Parsing del documento HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# Seleziona il tag <div> e scorrere i suoi elementi successivi
div_tag = soup.find('div')
for element in div_tag.next_elements:
    print(repr(element))

# '\n'
# <p>Questo è un paragrafo in un div.</p>
# 'Questo è un paragrafo in un div.'
# '\n'
# <ul>
# <li>Primo elemento della lista</li>
# <li>Secondo elemento della lista</li>
# <li>Terzo elemento della lista</li>
# </ul>
# '\n'
# <li>Primo elemento della lista</li>
# 'Primo elemento della lista'
# '\n'
# <li>Secondo elemento della lista</li>
# 'Secondo elemento della lista'
# '\n'
# <li>Terzo elemento della lista</li>
# 'Terzo elemento della lista'
# '\n'
# '\n'
# '\n'
# <p>Questo è un altro paragrafo.</p>
# 'Questo è un altro paragrafo.'
# '\n'
# '\n'
# '\n'