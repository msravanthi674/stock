import pandas as pd # type: ignore

def load_stock_data(file_path):
    data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return data