import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import json

exchange = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1h'

exchange = ccxt.binance()
markets = exchange.load_markets()
file_path = "data.json"
with open(file_path, "w") as json_file:
    json.dump(markets, json_file, indent=4)
print("Дата")