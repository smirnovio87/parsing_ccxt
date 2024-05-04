import json
from multiprocessing import Pool
import ccxt

#"binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"
name_exchanges = ['bitbank', 'binance', "bybit"]

def get_exchange_instance(id):
    exchange = getattr(ccxt, id)()
    return exchange

def fetch_ticker(args):
    try:
        id, exchange, symbol = args
        ticker = exchange.fetch_ticker(symbol)
    except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")    
            data[id] = "НЕ доступна"
                
    return id, ticker['last']

def price_result(name_exchanges):
    exchanges = {}
    with Pool() as pool:
        exchange_instances = pool.map(get_exchange_instance, name_exchanges)
        args = [(id, exchange, symbol) for id, exchange in zip(name_exchanges, exchange_instances)]
        data = dict(pool.starmap(fetch_ticker, args))
    return data

data_json = price_result(name_exchanges)

with open('btc_usdt_courses_12.json', 'w') as json_file:
    json.dump(data_json, json_file, indent=4)
print(data_json)