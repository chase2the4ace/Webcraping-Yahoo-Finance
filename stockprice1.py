import requests
from bs4 import BeautifulSoup

print("Using Yahoo Finance, submit a URL and the webscraping program will return the closing stock price, change in dollar amount, and the change in percent!")
print("The url must be in this format https://finance.yahoo.com/quote/(***Ticker Symbol***) ")

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = input("Input URL: ")

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
percent_change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text

print(price, change, percent_change)
