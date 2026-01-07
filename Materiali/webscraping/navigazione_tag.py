from bs4 import BeautifulSoup 
import requests 

url = "https://www.python.org/" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

print(soup.head)
# <head>
# <!-- Google tag (gtag.js) -->
# <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-TF35YF9CVH"></script>
# .......

print(soup.title)
# <title>Welcome to Python.org</title>

ls_a = soup.find_all('a')
print(ls_a[1])
# <a aria-hidden="true" class="jump-link" href="#python-network" id="close-python-network">
# <span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
#                 </a>
print(ls_a[2])
# <a class="current_item selectedcurrent_branch selected"
#  href="/" title="The Python Programming Language">Python</a>
