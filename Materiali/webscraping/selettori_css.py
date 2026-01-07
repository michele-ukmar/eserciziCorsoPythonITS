from bs4 import BeautifulSoup 
import requests 
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250" 
req = requests.get(url) 
soup = BeautifulSoup(req.text, "html.parser") 

# print(soup.select("p:nth-of-type(1)"))
# [<p>The Top Rated Movie list only includes feature films.</p>, 
# <p class="imdb-footer__copyright footer__copyright">© 1990-<!-- -->2023<!-- --> by IMDb.com, Inc.</p>]

sel = soup.select("div:nth-of-type(6)")

print(sel[0]['class'])
# ['sc-breuTD', 'gIvE', 'navlinkcat', 'noMarginItem']

print(sel[1]['class'])
# ['sc-iBkjds', 'sc-gXmSlM', 'iosfhR', 'kvlTHG', 'navbar__flyout--breakpoint-m']

print(sel[2]['class'])
# ['table-row']

# for s in sel:
#     print(s.text)

# print(soup.select("div:nth-of-type(6)"))
