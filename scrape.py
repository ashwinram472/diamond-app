import requests

import re
import argparse
import warnings
import pandas as pd


landing_page = requests.get('http://bluenile.com/')
url = 'https://www.bluenile.com/api/public/diamond-search-grid/v2?'

response = requests.get(url,params={'sortColumn': "price",'sortDirection': "asc"})


print(response.content)

startIndex=60&pageSize=50&_=1589679476182&unlimitedPaging=false&sortDirection=asc&sortColumn=default&shape=RD&\
maxDateType=MANUFACTURING_REQUIRED&isQuickShip=false&hasVisualization=false
&isFiltersExpanded=false&astorFilterActive=false&country=USA&language=en-us&currency=USD&productSet=BN'