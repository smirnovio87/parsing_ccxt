import ccxt
import pandas as pd

exchange = ccxt.bybit()
markets = exchange.load_markets()
symbol = "BTC/USDT"

def get_spread() -> pd.DataFrame:
    """
    функция get_spread_dataframe() возвращает DataFrame, который содержит данные о рассеянии (разнице между высокой и низкой ценами) для заданного символа за последний день.

    В DataFrame входят следующие столбцы:

    timestamp: метка времени каждого OHLCV-точки
    open: цена открытия
    high: наибольшая цена
    low: наименьшая цена
    close: цена закрытия
    volume: объем торгов
    spread: рассеяние в процентах (разница между наибольшей и наименьшей ценой)
    DataFrame индексирован по столбцу timestamp.
    """
    # Fetch the OHLCV data for the last day
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe="1d")

    # Create a DataFrame from the OHLCV data
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])

    # Convert the timestamp column to datetime objects
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", cache=True)

    # Calculate the spread (% difference between high and low prices)
    df["spread"] = (df["high"] - df["low"]) / df["low"] * 100

    # Set the timestamp column as the index
    return df.set_index("timestamp")

print(get_spread())