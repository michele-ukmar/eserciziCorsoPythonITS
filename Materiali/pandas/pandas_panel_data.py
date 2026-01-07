# pip install pandas-datareader

import pandas_datareader.data as web
from pandas_datareader import wb
import pandas_datareader as pdr

import pandas as pd
matches = wb.search('gdp.*capita.*const')
print(matches)

df = pdr.get_data_fred('GS10')
# get class type
print(type(df))

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)
print(type(dat))
print(dat)


