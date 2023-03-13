import requests
from bs4 import BeautifulSoup


def get_ticker():
    print("Input a Ticker Symbol and the price, change, and percent change of that stock will be returned: ")
    symbol = input()
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
        'percent change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock


print(get_ticker())
