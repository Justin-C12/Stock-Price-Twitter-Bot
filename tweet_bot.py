import tweepy
import time
from tweepy import api
import stock_info

stock_urls = [ 'https://finance.yahoo.com/quote/PENN/', 'https://finance.yahoo.com/quote/DK/', 'https://finance.yahoo.com/quote/GME/']
stock_name = []
stock_price = []

api_key = "vV93qzYOJ6yYAyu50CP2fH4HA"
api_secret_key = "o04X3VgkSxP6mMK1WMeaUVA1lCkwEZGpQnotWf9uayyPLpgOoE"
access_key ="1400462491310649347-m4tBUKnwQR3Zl1JlF97OA06T665zUl"
access_secret = "ItlbEdlcBgz0hus0ibMa3zozADVuFanLB4hAOQNfsOMIo"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)

twitter_API = tweepy.API(auth)

#if the time is equal to 9:30 AM
while True:
    if(time.localtime().tm_hour + time.localtime().tm_min + time.localtime().tm_sec == 39):
        for url in stock_urls:
            name = stock_info.StockInfo.getStockName(url)
            stock_name.append(name)
            price = stock_info.StockInfo.getStockPrice(url)
            stock_price.append(price)
        
        stock1_name = stock_name[0]
        stock2_name = stock_name[1]
        stock3_name = stock_name[2]

        stock1_price = stock_price[0]
        stock2_price = stock_price[1]
        stock3_price = stock_price[2]

        twitter_API.update_status(stock1_name + ": " + stock1_price + "\n" + stock2_name + ": " + stock2_price + "\n" + stock3_name + ": " + stock3_price)

    #if the time is equal to 11:30 AM
    if(time.localtime().tm_hour + time.localtime().tm_min + time.localtime().tm_sec == 41):
        for url in stock_urls:
            name = stock_info.StockInfo.getStockName(url)
            stock_name.append(name)
            price = stock_info.StockInfo.getStockPrice(url)
            stock_price.append(price)
        
        stock1_name = stock_name[0]
        stock2_name = stock_name[1]
        stock3_name = stock_name[2]

        stock1_price = stock_price[0]
        stock2_price = stock_price[1]
        stock3_price = stock_price[2]

        twitter_API.update_status(stock1_name + ": " + stock1_price + "\n" + stock2_name + ": " + stock2_price + "\n" + stock3_name + ": " + stock3_price)

    #if the time is equal to 1:30 PM
    if(time.localtime().tm_hour + time.localtime().tm_min + time.localtime().tm_sec == 43):
        for url in stock_urls:
            name = stock_info.StockInfo.getStockName(url)
            stock_name.append(name)
            price = stock_info.StockInfo.getStockPrice(url)
            stock_price.append(price)
        
        stock1_name = stock_name[0]
        stock2_name = stock_name[1]
        stock3_name = stock_name[2]

        stock1_price = stock_price[0]
        stock2_price = stock_price[1]
        stock3_price = stock_price[2]

        twitter_API.update_status(stock1_name + ": " + stock1_price + "\n" + stock2_name + ": " + stock2_price + "\n" + stock3_name + ": " + stock3_price)

    #if the time is equal to 3:30 PM
    if(time.localtime().tm_hour + time.localtime().tm_min + time.localtime().tm_sec == 45):
        for url in stock_urls:
            name = stock_info.StockInfo.getStockName(url)
            stock_name.append(name)
            price = stock_info.StockInfo.getStockPrice(url)
            stock_price.append(price)
        
        stock1_name = stock_name[0]
        stock2_name = stock_name[1]
        stock3_name = stock_name[2]

        stock1_price = stock_price[0]
        stock2_price = stock_price[1]
        stock3_price = stock_price[2]

        twitter_API.update_status(stock1_name + ": " + stock1_price + "\n" + stock2_name + ": " + stock2_price + "\n" + stock3_name + ": " + stock3_price)

    #if the time is equal to 4:30 PM
    if(time.localtime().tm_hour + time.localtime().tm_min + time.localtime().tm_sec == 46):
        for url in stock_urls:
            name = stock_info.StockInfo.getStockName(url)
            stock_name.append(name)
            price = stock_info.StockInfo.getStockPrice(url)
            stock_price.append(price)
        
        stock1_name = stock_name[0]
        stock2_name = stock_name[1]
        stock3_name = stock_name[2]

        stock1_price = stock_price[0]
        stock2_price = stock_price[1]
        stock3_price = stock_price[2]

        twitter_API.update_status(stock1_name + ": " + stock1_price + "\n" + stock2_name + ": " + stock2_price + "\n" + stock3_name + ": " + stock3_price)
