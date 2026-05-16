import matplotlib.pyplot as plt
import os

os.makedirs("images/charts", exist_ok=True)

def generate_price_chart(df, ticker):

    plt.figure(figsize=(15, 7))

    plt.plot(
        df["date"],
        df["close"],
        label="Close Price"
    )

    plt.plot(
        df["date"],
        df["sma20"],
        label="SMA20"
    )

    plt.plot(
        df["date"],
        df["sma50"],
        label="SMA50"
    )

    plt.title(f"{ticker} Stock Price")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    path = (
        f"images/charts/{ticker}_price_chart.png"
    )

    plt.savefig(path)

    plt.close()

    print(f"Saved: {path}")

def generate_return_chart(df, ticker):

    plt.figure(figsize=(14, 6))

    df["daily_return"].hist(
        bins=50
    )

    plt.title(
        f"{ticker} Return Distribution"
    )

    path = (
        f"images/charts/{ticker}_returns_chart.png"
    )

    plt.savefig(path)

    plt.close()

    print(f"Saved: {path}")

def generate_signal_chart(df, ticker):

    plt.figure(figsize=(15, 7))

    plt.plot(
        df["date"],
        df["close"],
        label="Close Price"
    )

    buy_signals = df[
        df["signal"] == "BUY"
    ]

    plt.scatter(
        buy_signals["date"],
        buy_signals["close"],
        marker="^"
    )

    plt.title(
        f"{ticker} BUY Signals"
    )

    path = (
        f"images/signals/{ticker}_signals.png"
    )

    os.makedirs(
        "images/signals",
        exist_ok=True
    )

    plt.savefig(path)

    plt.close()

    print(f"Saved: {path}")