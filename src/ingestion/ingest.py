import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt
import os


def generate_demo_data():

    print("\nUsing auto-generated demo stock data...\n")

    dates = pd.date_range(
        start="2023-01-01",
        periods=300
    )

    prices = np.cumsum(
        np.random.randn(300)
    ) + 150

    df = pd.DataFrame({
        "date": dates,
        "open": prices + np.random.randn(300),
        "high": prices + np.random.rand(300) * 2,
        "low": prices - np.random.rand(300) * 2,
        "close": prices,
        "adj_close": prices,
        "volume": np.random.randint(
            1000000,
            5000000,
            300
        )
    })

    return df


def fetch_stock_data(
    ticker="AAPL",
    start="2020-01-01"
):

    os.makedirs("data/raw", exist_ok=True)

    print(f"\nFetching stock data for {ticker}...\n")

    try:

        df = yf.download(
            ticker,
            start=start,
            end=dt.date.today().isoformat(),
            progress=False,
            auto_adjust=False
        )

        if df.empty:

            print(
                "\nYahoo Finance returned empty data."
            )

            df = generate_demo_data()

        else:

            df.reset_index(inplace=True)

            df.columns = [
                col.lower().replace(" ", "_")
                for col in df.columns
            ]

            if "adj_close" not in df.columns:
                df["adj_close"] = df["close"]

    except Exception as e:

        print(f"\nError fetching data: {e}")

        df = generate_demo_data()

    csv_path = f"data/raw/{ticker}_raw.csv"

    df.to_csv(csv_path, index=False)

    print(f"Raw data saved to {csv_path}")

    return df