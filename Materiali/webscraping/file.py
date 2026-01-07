
import os
from bs4 import BeautifulSoup 

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/python.html")
with open(file_dir) as fp: 
    soup = BeautifulSoup(fp, 'lxml') 
    print(soup)

# <!DOCTYPE html>
# <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]--><!--[if IE 7]>     
# <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]--><!--[if IE 8]>      <html class="no-js ie8 lt-ie9"> 
# <![endif]--><!--[if gt IE 8]><!--><html class="no-js" dir="ltr" lang="en"> <!--<![endif]-->
# <head>
# <!-- Google tag (gtag.js) -->
# <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-TF35YF9CVH"></script>
# <script>


soup = BeautifulSoup("<html>data</html>") 
print(soup)
# Output: <html><body><p>data</p></body></html>

html = '''<b>tutorialspoint</b>, <i>&web scraping &data science;</i>''' 
soup = BeautifulSoup(html, 'lxml') 
print(soup) 
# Output 
# <html><body><b>tutorialspoint</b>, <i>&amp;web scraping &amp;data science;</i></body></html> 
