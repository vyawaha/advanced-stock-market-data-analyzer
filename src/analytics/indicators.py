from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

def calculate_indicators(df):

    print("\nCalculating indicators...\n")

    df["daily_return"] = (
        df["close"].pct_change()
    )

    df["sma20"] = SMAIndicator(
        close=df["close"],
        window=20
    ).sma_indicator()

    df["sma50"] = SMAIndicator(
        close=df["close"],
        window=50
    ).sma_indicator()

    df["rsi14"] = RSIIndicator(
        close=df["close"],
        window=14
    ).rsi()

    df["volatility"] = (
        df["daily_return"]
        .rolling(20)
        .std()
    )

    return df