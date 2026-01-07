from bs4 import BeautifulSoup
html_markup = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>
<META HTTP-EQUIV="content-type" CONTENT="text/html; charset=iso-8859-2"> </HEAD>
<BODY>
ąćęłńóśźżĄĆĘŁŃÓŚŹŻ
</BODY>
</HTML>
"""
soup = BeautifulSoup(html_markup)
print(soup.prettify())
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> <html>
# <head>
# <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
#   </head>
#   <body>
# ąćęłńóśźżĄĆĘŁŃÓŚŹŻ </body>
# </html>

print(soup.prettify("latin-1"))
# b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n<html>\n <head>\n <meta content="text/html; charset=latin-1" http-equiv="content- type"/>\n </head>\n <body>\n &#261; &#263; &#281; &#322; &#324; \xf3 &#347; &#378; &#380; &#260; &#262; &#280; &#321; &#323; \xd3 &#346; &#377; &#379;\n </body>\n</html>\n'

print(soup.body.encode("latin-1"))
# b'\n&#261; &#263; &#281; &#322; &#324; \xf3 &#347; &#378; &#380; &#260; &#262; &#280; &#321; &#323; \xd3 &#346; &#377; &#379;\n'
