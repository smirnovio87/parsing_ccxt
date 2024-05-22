import ccxt
import pandas as pd

symbol = 'BTC/USDT'
exchange = ccxt.binance()
ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d')
df=pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
prices=df['close']

def detect_trend(prices):
    # Вычисляем изменения цен между последовательными днями
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

#Считаем количество положительных и отрицательных изменений
    positive_changes = sum(1 for change in changes if change > 0)
    negative_changes = sum(1 for change in changes if change < 0)

#Определяем тренд
    if positive_changes > negative_changes:
        trend = "Восходящий"
    elif positive_changes < negative_changes:
        trend = "Нисходящий"
    else:
        trend = "Боковой"

    return trend

#Пример данных (цены закрытия за несколько дней)
#prices = [100, 110, 120, 115, 118, 122, 130, 135, 132, 140]

#Определение тренда на основе данных
trend = detect_trend(prices)
print("Тренд:", trend)