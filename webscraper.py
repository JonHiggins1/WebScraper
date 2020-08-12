from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print (content)
