import os
from bs4 import BeautifulSoup
import pandas as pd
import requests
import locale 


page_link ='https://www.ebay.it/sch/i.html?_nkw=iphone'


page_response = requests.get(page_link, timeout=5)

print(page_response.status_code)
page_content = BeautifulSoup(page_response.content, "html.parser")
# get page locale from html tag
locale_of_page = page_content.find('html')['lang']
print(locale_of_page)

pagination_items = page_content.find_all(attrs={'class': 'pagination__item'})

df = pd.DataFrame()
pg_texts = set()

# iterate as many times as there are pages
while len(pagination_items) > 0:
    title = page_content.find_all('div', attrs={'class': 's-item__title'})
    prices = page_content.find_all('span', attrs={'class': 's-item__price'})
    print(len(title))
    print(len(prices))
    annunci = { i:( title[i].text, prices[i].text ) for i in range(len(title))}
    print(annunci)
    df_local = pd.DataFrame.from_dict(annunci, orient='index', columns=['title', 'price'])
    # apply a lambda function to add the currency column using the price column
    df_local['currency'] = df_local['price'].apply(lambda x: 'EUR' if ('EUR' in x)  else '$' if ('$' in x) else x)
    df_local['price'] = df_local['price'].str.replace('EUR', '').str.replace('$', '')
    # get the decimal separator knowing the locale
    locale.setlocale(locale.LC_ALL, "it_IT.UTF-8")
    # replace the decimal separator with a dot
    df_local['price'] = df_local['price'].str.replace(locale.localeconv()['decimal_point'], '.')
    # try to convert price to float or set NA if not possible for each value
    df_local['price'] = pd.to_numeric(df_local['price'], errors='coerce')
    df_local['price'] = df_local['price'].astype(float)
    # concatenate dataframes
    df = pd.concat([df, df_local])
    print(df.info())

    pg_texts.add(pagination_items[0].text)
    pagination_items = page_content.find_all(attrs={'class': 'pagination__item'})
    # remove from pagination_items the element where text is in pg_texts
    pagination_items = [x for x in pagination_items if x.text not in pg_texts]
    if(len(pagination_items) > 0):
        new_link = pagination_items[0].get('href')
        print(new_link)

    page_response = requests.get(new_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

# write datafarme to excel
local_file = os.path.join(os.path.dirname(__file__),"web_scraping_esercizio_2.xlsx")
df.to_excel(local_file, index=False)

# write dataframe to csv
local_file = os.path.join(os.path.dirname(__file__),"web_scraping_esercizio_2.csv")
df.to_csv(local_file, index=False)