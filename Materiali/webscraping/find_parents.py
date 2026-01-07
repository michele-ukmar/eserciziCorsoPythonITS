from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250" 
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

a_string = soup.find(name='a', string=["The Godfather","Il padrino"])

print(a_string)
# <a href="/title/tt0068646/" title="Francis Ford Coppola (dir.), Marlon Brando, Al Pacino">Il padrino</a>

print(a_string.find_parent('a'))
# None

print(a_string.find_parents('a'))
# []

print(a_string.find_parent('tr'))
# <tr>
# <td class="posterColumn">
# <span data-value="2" name="rk"></span>
# <span data-value="9.15576245640774" name="ir"></span>
# <span data-value="6.93792E10" name="us"></span>
# <span data-value="1898949" name="nv"></span>
# <span data-value="-1.8442375435922607" name="ur"></span>
# <a href="/title/tt0068646/"> <img alt="Il padrino" height="67" src="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg" width="45"/>
# </a> </td>
# <td class="titleColumn">
#       2.
#       <a href="/title/tt0068646/" title="Francis Ford Coppola (dir.), Marlon Brando, Al Pacino">Il padrino</a>
# <span class="secondaryInfo">(1972)</span>
# </td>
# <td class="ratingColumn imdbRating">
# <strong title="9.2 based on 1,898,949 user ratings">9.2</strong>
# </td>
# <td class="ratingColumn">
# <div class="seen-widget seen-widget-tt0068646 pending" data-titleid="tt0068646">
# <div class="boundary">
# <div class="popover">
# <span class="delete"> </span><ol><li>1<li>2<li>3<li>4<li>5<li>6<li>7<li>8<li>9<li>10</li></li></li></li></li></li></li></li></li></li></ol> </div>
# </div>
# <div class="inline">
# <div class="pending"></div>
# <div class="unseeable">NOT YET RELEASED</div>
# <div class="unseen"> </div>
# <div class="rating"></div>
# <div class="seen">Seen</div>
# </div>
# </div>
# </td>
# <td class="watchlistColumn">
# <div class="wlb_ribbon" data-recordmetrics="true" data-tconst="tt0068646"></div>
# </td>
# </tr>