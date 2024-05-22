import ccxt
import pandas as pd

exchange = ccxt.bybit()
markets = exchange.load_markets()
symbol = "BTC/USDT"

def get_spread_dataframe():
    """
    Returns a dataframe with the spread of the given symbol over the last 1 day.

    The dataframe contains the following columns:
    - timestamp: the timestamp of each OHLCV point
    - open: the open price
    - high: the high price
    - low: the low price
    - close: the close price
    - volume: the trading volume
    - spread: the spread as a percentage (difference between high and low prices)

    The dataframe is indexed by the timestamp column.
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

print(get_spread_dataframe())