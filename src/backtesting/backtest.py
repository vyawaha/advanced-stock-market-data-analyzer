import numpy as np


def run_backtest(df):

    print("\nRunning backtest...\n")

    if df.empty:

        print("ERROR: Empty dataframe")

        return {
            "market_return": 0,
            "strategy_return": 0
        }

    df["strategy_return"] = np.where(
        df["signal"] == "BUY",
        df["daily_return"],
        0
    )

    df["daily_return"] = (
        df["daily_return"]
        .fillna(0)
    )

    df["strategy_return"] = (
        df["strategy_return"]
        .fillna(0)
    )

    cumulative_market = (
        1 + df["daily_return"]
    ).cumprod()

    cumulative_strategy = (
        1 + df["strategy_return"]
    ).cumprod()

    market_return = (
        cumulative_market.iloc[-1] - 1
    ) * 100

    strategy_return = (
        cumulative_strategy.iloc[-1] - 1
    ) * 100

    return {
        "market_return": market_return,
        "strategy_return": strategy_return
    }