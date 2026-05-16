from src.ingestion.ingest import fetch_stock_data

from src.analytics.indicators import calculate_indicators

from src.analytics.signals import generate_signals

from src.analytics.risk_analysis import risk_analysis

from src.backtesting.backtest import run_backtest

from src.visualization.charts import (
    generate_price_chart,
    generate_return_chart,
    generate_signal_chart
)

from src.utils.helpers import create_folders


def main():

    create_folders()

    ticker = "AAPL"

    df = fetch_stock_data(ticker)

    df = calculate_indicators(df)

    df = generate_signals(df)

    risk = risk_analysis(df)

    backtest = run_backtest(df)

    processed_csv = (
        f"outputs/csv/{ticker}_processed.csv"
    )

    df.to_csv(
        processed_csv,
        index=False
    )

    print(f"\nSaved: {processed_csv}")

    generate_price_chart(df, ticker)

    generate_return_chart(df, ticker)

    generate_signal_chart(df, ticker)

    report_path = (
        f"outputs/reports/{ticker}_report.txt"
    )

    with open(report_path, "w") as file:

        file.write(
            "ADVANCED STOCK MARKET REPORT\n"
        )

        file.write(
            "============================\n\n"
        )

        file.write(
            f"Ticker: {ticker}\n\n"
        )

        file.write(
            f"Average Return: "
            f"{risk['average_return']:.6f}\n"
        )

        file.write(
            f"Volatility: "
            f"{risk['volatility']:.6f}\n"
        )

        file.write(
            f"Maximum Return: "
            f"{risk['max_return']:.6f}\n"
        )

        file.write(
            f"Minimum Return: "
            f"{risk['min_return']:.6f}\n\n"
        )

        file.write(
            f"Market Return: "
            f"{backtest['market_return']:.2f}%\n"
        )

        file.write(
            f"Strategy Return: "
            f"{backtest['strategy_return']:.2f}%\n"
        )

    print(f"\nSaved: {report_path}")

    print("\nPROJECT EXECUTED SUCCESSFULLY\n")


if __name__ == "__main__":
    main()