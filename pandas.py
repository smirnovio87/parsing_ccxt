import ccxt
import pandas as pd

def get_spred():
    exchange = ccxt.bybit()
    markets = exchange.load_markets()
    symbol = "BTC/USDT"
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe="1d")
    df = pd.DataFrame(ohlcv, columns=["datetime", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")
    df["spread"] = (df["high"] - df["low"]) / df["low"] * 100
    return df

print(get_spred)