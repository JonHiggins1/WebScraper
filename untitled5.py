# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:19:49 2020

@author: jhigg
"""


from bs4 import BeautifulSoup
import requests
import json
"""import requests from bs4 """
import csv 
import pandas as pd 
"""
url = 'https://www.google.com/finance?tab=yourstocks&sa=X&ved=0CAQQx-cFahcKEwjwlK2umJTrAhUAAAAAHQAAAAAQAQ'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

stockArr = []
for stock in content.findAll('div', attrs={"class": "stockcontainer"}):
    stockObject = {
        "dB5gr ": stock.find('h2', attrs={"class": "dB5gr "}).text.encode('utf-8'),
        "vjQh1d ": stock.find('h5', attrs={"class": "vjQh1d "}).text.encode('utf-8'),
        "TVTUyf ": stock.find('p', attrs={"class": "TVTUyf "}).text.encode('utf-8'),
        "LFD83d": stock.find('p', attrs={"class": "LFD83d"}).text.encode('utf-8'),
        "s7JTO": stock.find('p', attrs={"class": "s7JTO"}).text.encode('utf-8')
    }

stockArr = []
for stock in content.findAll('div', attrs={"class": "stockcontainer"}):
    stockObject = {
        "XPk1dd": stock.find('jscontroller', attrs={"class": "XPk1dd"}).text.encode('utf-8'),
        "szkiI": stock.find('jscontroller', attrs={"class": "szkiI"}).text.encode('utf-8')
    }
    
stockArr = []
for stock in content.findAll('div jscontroller', attrs={"class": "stockcontainer"}):
    stockObject = {
        "E90kee": stock.find('jscontroller', attrs={"class": "E90kee"}).text.encode('utf-8') 
        "ZV79P": stock.find('jscontroller', attrs={"class": "E90kee"}).text.encode('utf-8')
    }"""

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
 
for i in range(0,11):
 CryptoCurrenciesUrl = "https://in.finance.yahoo.com/most-active?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=100"
r= requests.get(CryptoCurrenciesUrl)
data=r.text
soup=BeautifulSoup(data, "lxml")
 
for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
   for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
   for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
   for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
   for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
   for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
   for totalVolume in listing.find_all('td', attrs={'aria-label':'Avg vol (3-month)'}):
      totalVolumes.append(totalVolume.text)
   for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Volume'}):
      circulatingSupplys.append(circulatingSupply.text)
 
pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys})   
 
"""   
    stockArr.append(stockObject)
with open('stockData.json', 'w') as outfile:
    json.dump(stackArr, outfile)
    """