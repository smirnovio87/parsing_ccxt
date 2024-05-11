
import ccxt
import json
# Получает пару BTC/USDT на нескольких биржах и записывает ее в json

# "binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"

name_exchanges = ["binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"]
symbol = 'BTC/USDT'

exchanges = {}
for id in name_exchanges:
    #getattr возврашает значение атрибута по имени этого атрибута. 
    #Т.Е. Вернет обект ccxt с атрибутом binance - ccxt.binance
    exchange = getattr(ccxt, id)
    #Данной строкой записываем в словарь exchanges id {"binance": ccxt.binance} ну и так по всем name_exchanges
    exchanges[id] = exchange()
print (exchanges)

data = {}

for id, exchange in exchanges.items():
    ticker = exchange.fetch_ticker(symbol)
    #Записываем в словарь к ключу [id]-название биржы = значение exchange.fetch_ticker(symbol) - "last"
    data[id] = ticker['last']

#Записываем в Json файл
with open('btc_usdt_courses_all.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
print(data)