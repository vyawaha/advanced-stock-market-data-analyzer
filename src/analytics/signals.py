import numpy as np

def generate_signals(df):

    print("\nGenerating trading signals...\n")

    df["signal"] = np.where(
        df["sma20"] > df["sma50"],
        "BUY",
        "SELL"
    )

    return df