import ccxt
import pandas as pd



def get_spred():
    """
    Retrieves the spread (% difference between high and low prices) for the
    BTC/USDT pair over the last day and returns it in a pandas DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame containing the datetime, open, high, low,
        close, and volume for each minute of the last day. Additionally, it
        includes a 'spread' column which is the percentage difference between
        the high and low prices.
    """
    # Create an instance of the Bybit exchange
    exchange = ccxt.bybit()

    # Load the markets for the exchange
    markets = exchange.load_markets()

    # Define the symbol we want to retrieve data for
    symbol = "BTC/USDT"

    # Retrieve the OHLCV data for the last day
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe="1d")

    # Create a DataFrame from the OHLCV data
    df = pd.DataFrame(ohlcv, columns=["datetime", "open", "high", "low", "close", "volume"])

    # Convert the datetime column to datetime objects
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")

    # Calculate the spread (% difference between high and low prices)
    df["spread"] = (df["high"] - df["low"]) / df["low"] * 100

    # Return the DataFrame
    return df


print(get_spred())