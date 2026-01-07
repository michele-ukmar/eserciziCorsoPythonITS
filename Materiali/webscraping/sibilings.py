from bs4 import BeautifulSoup
h_s ="<a>\
        <b>Hello Pyhton</b>\
        <c>\
            <strong>the simplest coding language</strong>\
        </c>\
    </a>" 
sibling_soup = BeautifulSoup(h_s, 'lxml')
print(sibling_soup.prettify())
# <html>
#  <body>
#   <a>
#    <b>
#     Hello Pyhton
#    </b>
#    <c>
#     <strong>
#      the simplest coding language
#     </strong>
#    </c>
#   </a>
#  </body>
# </html>