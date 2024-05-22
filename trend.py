import ccxt
import pandas as pd

symbol = 'BTC/USDT'
exchange = ccxt.binance()
ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d')
df=pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
prices=df['close']

def detect_trend(prices: list[float]) -> str: 
    """
    Определяет тренд заданного списка цен.

    """

    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]


    positive_changes = sum(1 for change in changes if change > 0)
    negative_changes = sum(1 for change in changes if change < 0)

    if positive_changes > negative_changes:
        trend = "Восходящий"
    elif positive_changes < negative_changes:
        trend = "Нисходящий"
    else:
        trend = "Боковой"

    return trend

trend = detect_trend(prices)
print("Тренд:", trend)