import ccxt
import pandas as pd

exchange = ccxt.bybit()
markets = exchange.load_markets()
symbol = "BTC/USDT"
def get_spread_dataframe():
    """Returns a dataframe with the spread of the given symbol over the last 1 day."""
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe="1d")
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", cache=True)
    df["spread"] = (df["high"] - df["low"]) / df["low"] * 100
    return df.set_index("timestamp")

print(get_spread_dataframe())