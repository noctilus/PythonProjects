# Import libraries
import json
import requests

# defining key/request url
DOT = 13.89568028
FLOW = 7.15629868
ETH = 0.01225312
QNT = 0.16354939
DOGE = 299.68802015
ATOM = 1.798079
total_value = 0

tickers = {'DOT': DOT, 'FLOW': FLOW, 'ETH': ETH,
           'QNT': QNT, 'DOGE': DOGE, 'ATOM': ATOM}

api_url = "https://api.binance.com/api/v3/ticker/price?symbol="

for key in tickers:
    print(key, tickers[key])
    data = requests.get(api_url+key+"USDT")
    data = data.json()
    coin_value = round(tickers[key]*float(data['price']), 2)

    print(f"{tickers[key]}:" + str(coin_value))
    total_value = total_value+coin_value

print(round((total_value), 2))

# requesting data from url
# data = requests.get(key)
# data = data.json()
# print(f"{data['symbol']} price is {data['price']}")
