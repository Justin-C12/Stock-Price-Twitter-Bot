
import bs4
import requests
from bs4 import BeautifulSoup


class StockInfo:

    def getStockPrice(url):
        stock = requests.get(url)
        soup = bs4.BeautifulSoup(stock.text, features="html.parser")
        price = soup.find("div",{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        return price
        
    def getStockName(url):
        stock = requests.get(url)
        soup = bs4.BeautifulSoup(stock.text, features="html.parser")
        name = soup.find("div", {'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find('h1').text
        return name
   

