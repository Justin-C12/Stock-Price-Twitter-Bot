import bs4
import requests
from bs4 import BeautifulSoup
import time

url = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup = bs4.BeautifulSoup(url.text, features="html.parser")
price = soup.find("div",{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
print(price)

