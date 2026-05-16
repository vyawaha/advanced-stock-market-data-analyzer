import os

def create_folders():

    folders = [
        "outputs/csv",
        "outputs/reports",
        "outputs/backtests",
        "images/charts",
        "images/reports",
        "images/signals"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)