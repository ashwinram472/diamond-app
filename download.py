import json
import pandas as pd
import re
import requests
import argparse
import warnings
import time


def _price_to_int(s):
    return int(re.sub('[\$,\[\]\']','',str(s)))

def diamonds():
    start_time = time.time()
    print("The start time is:",start_time)
    i=0
    df = []
    count = 0
    while True:
        url = 'https://www.bluenile.com/api/public/diamond-search-grid/v2?startIndex=0&pageSize=1000&_=1590100374198&unlimitedPaging=false&sortDirection=asc&sortColumn=default&shape=RD,PR,EC,AS,CU,MQ,RA,OV,PS,HS&minPrice='+str(i)+'&maxDateType=MANUFACTURING_REQUIRED&isQuickShip=false&hasVisualization=false&isFiltersExpanded=false&astorFilterActive=false&country=USA&language=en-us&currency=USD&productSet=BN'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            df += data['results']

            min_price = data['results'][0]['price']
            
            max_price = data['results'][-1]['price']
            
            
            print('The min price now is:',min_price,'its now changed to :',max_price)

            min_price = max_price
            j = i
            i = _price_to_int(min_price)
            
            if i==j:
                print('end')
                break
            print("changed i is",i)
            count += 1
        elif response.status_code != 200 :
            time.sleep(5)
            continue
        elif min_price == max_price:
            print('_________________end reached___________________')
            break
        
    with open('C:\Work\Github\diamond\mamba.json','w') as file:
        json.dump(df,file)
    print("The total api requests are : ",count)
    print("The total time taken is:", time.time() - start_time)

diamonds()


