
import ccxt
import json

# "binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"

#name_exchanges = ["binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"]
name_exchanges = ccxt.exchanges
name_exchanges = ['bitbank', 'binance']

symbol = 'BTC/USDT'

def price_result(name_exchanges):
    exchanges = {}
    for id in name_exchanges:
        #getattr возврашает значение атрибута по имени этого атрибута. 
        #Т.Е. Вернет обект ccxt с атрибутом binance - ccxt.binance
        exchange = getattr(ccxt, id)
        #Данной строкой записываем в словарь exchanges id {"binance": ccxt.binance} ну и так по всем name_exchanges
        exchanges[id] = exchange()
    print(exchanges)

    data = {}

    for id, exchange in exchanges.items():
        try: 
            ticker = exchange.fetch_ticker(symbol)
            data[id] = ticker['last']
        except Exception as err:
        #Записываем в словарь к ключу [id]-название биржы = значение exchange.fetch_ticker(symbol) - "last"
            print(f"Unexpected {err=}, {type(err)=}")    
            data[id] = "НЕ доступна"
        
    return data

data_json=price_result(name_exchanges)
#Записываем в Json файл
with open('btc_usdt_courses_12.json', 'w', encoding="utf-8") as json_file:

    json.dump(data_json, json_file, indent=4, ensure_ascii=False)
print(data_json)