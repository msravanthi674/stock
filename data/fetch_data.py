import yfinance as yf # type: ignore
import pandas as pd # type: ignore

def download_stock_data(ticker="AAPL", start="2020-01-01", end="2023-12-31"):
    data = yf.download(ticker, start=start, end=end)
    data.to_csv(f"data/{ticker}_stock.csv")
    print(f"Data saved to data/{ticker}_stock.csv")
    return data

if __name__ == "__main__":
    download_stock_data("AAPL")