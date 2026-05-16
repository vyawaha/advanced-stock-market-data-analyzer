from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(
    title="Advanced Stock Market Data Analyzer API",
    description="""
Professional FastAPI backend for stock market analytics,
technical indicators, trading signals,
risk analysis, and backtesting.
""",
    version="1.0.0"
)

# ---------------------------------------------------
# CORS CONFIGURATION
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# FILE PATHS
# ---------------------------------------------------

CSV_PATH = "outputs/csv/AAPL_processed.csv"

REPORT_PATH = (
    "outputs/reports/AAPL_report.txt"
)

# ---------------------------------------------------
# HOME ENDPOINT
# ---------------------------------------------------

@app.get("/")
def home():

    return {
        "message":
        "Advanced Stock Market Data Analyzer API Running Successfully"
    }

# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

# ---------------------------------------------------
# STOCK DATA ENDPOINT
# ---------------------------------------------------

@app.get("/stock-data")
def stock_data():

    if not os.path.exists(CSV_PATH):

        return {
            "error":
            "Processed CSV not found. Run main.py first."
        }

    df = pd.read_csv(CSV_PATH)

    return df.tail(50).to_dict(
        orient="records"
    )

# ---------------------------------------------------
# SUMMARY ENDPOINT
# ---------------------------------------------------

@app.get("/summary")
def summary():

    if not os.path.exists(CSV_PATH):

        return {
            "error":
            "CSV file not found."
        }

    df = pd.read_csv(CSV_PATH)

    latest = df.iloc[-1]

    summary_data = {

        "latest_close_price":
        float(latest.get("close", 0)),

        "latest_open_price":
        float(latest.get("open", 0)),

        "latest_high_price":
        float(latest.get("high", 0)),

        "latest_low_price":
        float(latest.get("low", 0)),

        "latest_volume":
        int(latest.get("volume", 0)),

        "latest_signal":
        str(latest.get("signal", "HOLD")),

        "latest_daily_return":
        float(latest.get("daily_return", 0)),

        "50_day_moving_average":
        float(latest.get("SMA_50", 0)),

        "200_day_moving_average":
        float(latest.get("SMA_200", 0)),

        "rsi":
        float(latest.get("RSI", 0)),

        "macd":
        float(latest.get("MACD", 0))
    }

    return summary_data

# ---------------------------------------------------
# RISK ANALYSIS ENDPOINT
# ---------------------------------------------------

@app.get("/risk-analysis")
def risk_analysis():

    if not os.path.exists(CSV_PATH):

        return {
            "error":
            "CSV file not found."
        }

    df = pd.read_csv(CSV_PATH)

    risk_data = {

        "average_daily_return":
        float(df["daily_return"].mean()),

        "volatility":
        float(df["daily_return"].std()),

        "maximum_daily_return":
        float(df["daily_return"].max()),

        "minimum_daily_return":
        float(df["daily_return"].min()),

        "total_records":
        int(len(df))
    }

    return risk_data

# ---------------------------------------------------
# SIGNAL ANALYSIS ENDPOINT
# ---------------------------------------------------

@app.get("/signals")
def signals():

    if not os.path.exists(CSV_PATH):

        return {
            "error":
            "CSV file not found."
        }

    df = pd.read_csv(CSV_PATH)

    buy_signals = len(
        df[df["signal"] == "BUY"]
    )

    sell_signals = len(
        df[df["signal"] == "SELL"]
    )

    hold_signals = len(
        df[df["signal"] == "HOLD"]
    )

    return {

        "buy_signals":
        buy_signals,

        "sell_signals":
        sell_signals,

        "hold_signals":
        hold_signals
    }

# ---------------------------------------------------
# BACKTEST REPORT ENDPOINT
# ---------------------------------------------------

@app.get("/backtest")
def backtest():

    if not os.path.exists(REPORT_PATH):

        return {
            "error":
            "Backtest report not found."
        }

    with open(
        REPORT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        report = file.read()

    return {
        "report": report
    }

# ---------------------------------------------------
# CHART STATUS ENDPOINT
# ---------------------------------------------------

@app.get("/charts")
def charts():

    charts = {

        "price_chart":
        os.path.exists(
            "images/charts/AAPL_price_chart.png"
        ),

        "returns_chart":
        os.path.exists(
            "images/charts/AAPL_returns_chart.png"
        ),

        "signals_chart":
        os.path.exists(
            "images/signals/AAPL_signals.png"
        )
    }

    return charts

# ---------------------------------------------------
# PROJECT INFORMATION ENDPOINT
# ---------------------------------------------------

@app.get("/project-info")
def project_info():

    return {

        "project":
        "Advanced Stock Market Data Analyzer",

        "technology_stack": [

            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "FastAPI",
            "yFinance",
            "Technical Analysis",
            "Backtesting"
        ],

        "features": [

            "Automated stock data fetching",
            "Technical indicator calculation",
            "Trading signal generation",
            "Risk analysis",
            "Backtesting engine",
            "Automated chart generation",
            "REST API endpoints",
            "Financial analytics"
        ],

        "disclaimer":
        "This project is for educational purposes only and not financial advice."
    }

# ---------------------------------------------------
# STARTUP MESSAGE
# ---------------------------------------------------

@app.on_event("startup")
def startup_message():

    print(
        "\nAdvanced Stock Market API Started Successfully\n"
    )