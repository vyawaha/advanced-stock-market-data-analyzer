def risk_analysis(df):

    avg_return = df["daily_return"].mean()

    volatility = df["daily_return"].std()

    max_return = df["daily_return"].max()

    min_return = df["daily_return"].min()

    return {
        "average_return": avg_return,
        "volatility": volatility,
        "max_return": max_return,
        "min_return": min_return
    }