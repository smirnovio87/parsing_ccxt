import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1h'

tiker = exchange.fetch_ticker(symbol)
print("Курс Биткоина к доллару: ", tiker["last"])

ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
 
print(df.head())

plt.plot(df['timestamp'], df['close'])
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.title('График цены закрытия BTC/USDT')
plt.show()

# exchange = ccxt.binance()
# markets = exchange.load_markets()
# print(markets)

