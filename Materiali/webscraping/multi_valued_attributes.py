from bs4 import BeautifulSoup 
css_soup = BeautifulSoup('<p class="body"></p>')  
print(css_soup.p['class'])

# ['body']

css_soup = BeautifulSoup('<p class="body bold"></p>')  
print(css_soup.p['class'])
# ['body', 'bold']


id_soup = BeautifulSoup('<p ciao="body bold"></p>')
print(id_soup.p['ciao'])
# 'body bold'

print(type(id_soup.p['ciao']))
# <class 'str'>

rel_soup = BeautifulSoup("<p> Tag di test <a rel='Index'> Page</a></p>", 'lxml')
print(rel_soup.a['rel'])
# ['Index']

rel_soup.a['rel'] = ['Index', ' Machine Learning and Big data']
print(rel_soup.p)
# <p> Tag di test <a rel="Index  Machine Learning and Big data"> Page</a></p>

print(id_soup.p.get_attribute_list('ciao'))

xml_soup = BeautifulSoup('<p class="body bold"></p>', 'xml')
print(xml_soup.p['class'])
#  'body bold'