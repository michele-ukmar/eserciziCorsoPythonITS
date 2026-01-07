
from bs4 import BeautifulSoup

markup = b"<h1>\xed\xe5\xec\xf9</h1>" 
soup = BeautifulSoup(markup, exclude_encodings=["ISO-8859-7"])
print(soup.h1)
# <h1>םולש</h1>
print(soup.original_encoding)
'iso-8859-8'
