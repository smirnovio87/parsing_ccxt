import ccxt
import json
from multiprocessing import Pool, freeze_support

# "binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"
name_exchanges = ["binance", "bybit", "coinex", "kraken"]
symbol = 'BTC/USDT'

def get_exchange_instance(id):
    exchange = getattr(ccxt, id)()
    return exchange

def fetch_ticker(args):
    exchange, symbol = args
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def price_result(name_exchanges):
    exchanges = {}
    with Pool() as pool:
        exchange_instances = pool.map(get_exchange_instance, name_exchanges)
        args = [(exchange, symbol) for exchange in exchange_instances]
        data = pool.map(fetch_ticker, args)
    return dict(zip(name_exchanges, data))

if __name__ == '__main__':
    freeze_support()  # Required for Windows when using multiprocessing
    data_json = price_result(name_exchanges)
    print("Test", data_json)