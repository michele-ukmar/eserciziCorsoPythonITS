from bs4 import BeautifulSoup

markup = BeautifulSoup('<p>Top Three</p><p><pre>Programming Languages are:</pre></p><p><b>Java, Python, Cplusplus</b></p>', 'lxml')

print(markup.find_all('p'))
# [<p>Top Three</p>, <p></p>, <p><b>Java, Python, Cplusplus</b></p>]

import re
markup = BeautifulSoup('<p>Top Three</p><p><pre>Programming Languages are:</pre></p><p><b>Java, Python, Cplusplus</b></p>')

print(markup.find_all(re.compile('^p')))
# [<p>Top Three</p>, <p></p>, <pre>Programming Languages are:</pre>, <p><b>Java, Python, Cplusplus</b></p>]

markup = BeautifulSoup('<p>Top Three</p><p><pre>Programming Languages are:</pre></p><p><b>Java, Python, Cplusplus</b></p>')
print(markup.find_all(['pre', 'b']))
# [<pre>Programming Languages are:</pre>, <b>Java, Python, Cplusplus</b>]

markup = BeautifulSoup('<p>Top Three</p><p><pre>Programming Languages are:</pre></p><p><b>Java, Python, Cplusplus</b></p>')
print(markup.find_all(True))
# [<html><body><p>Top Three</p><p>
# </p><pre>Programming Languages are:</pre><p><b>Java,
#  Python, Cplusplus</b></p></body></html>, <body>
# <p>Top Three</p><p></p><pre>Programming Languages are:</pre>
# <p><b>Java, Python, Cplusplus</b></p></body>, <p>Top Three</p>, 
# <p></p>, 
# <pre>Programming Languages are:</pre>, 
# <p><b>Java, Python, Cplusplus</b></p>, 
# <b>Java, Python, Cplusplus</b>]

for tag in markup.find_all(True):
    print(tag.name)
# html
# body
# p
# p
# pre
# p
# b

for tag in markup.find_all(True):
    print(tag.string)
# None
# None
# Top Three
# None
# Programming Languages are:
# Java, Python, Cplusplus
# Java, Python, Cplusplus