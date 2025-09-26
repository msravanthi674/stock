# 📈 Stock Price Predictor

A Machine Learning project that predicts stock prices using historical market data.  
This project demonstrates time-series forecasting and regression techniques using Python and popular ML libraries.

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Libraries](https://img.shields.io/badge/Libraries-Pandas%2C%20NumPy%2C%20Scikit--Learn-yellow?logo=python&logoColor=white)](https://scikit-learn.org/)
[![yFinance](https://img.shields.io/badge/Data-yFinance-lightgrey?logo=yahoo&logoColor=purple)](https://pypi.org/project/yfinance/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)

---

## 🚀 Features

- Fetch historical stock data from Yahoo Finance using `yfinance`.
- Preprocess and explore data (missing values, moving averages).
- Train a **Linear Regression** model to predict closing prices.
- Evaluate performance using **RMSE** and **R² Score**.
- Visualize actual vs predicted stock prices.
- Predict future stock closing prices for any ticker symbol.

---

## 📂 Project Structure
```bash
Stock-Price-Predictor/
│── data/ # Stock data CSV files or fetch_data.py
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Python modules
│ │── data_loader.py
│ │── model.py
│ │── evaluate.py
│── requirements.txt
│── environment.yml
│── README.md
│── LICENSE
```
---

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Stock-Price-Predictor.git
cd Stock-Price-Predictor
```
### 2. Create Conda Environment
```bash
conda env create -f environment.yml
conda activate stock_predictor
```
### 3. (Optional) Install using pip
```bash
pip install -r requirements.txt
```
▶️ Usage
### 1. Fetch stock data
```bash
python data/fetch_data.py
```
Downloads data for the specified ticker (default: AAPL).

Saved to data/AAPL_stock.csv.

### 2. Run Jupyter Notebook
```bash
jupyter notebook notebooks/stock_predictor.ipynb
```
Explore data, train model, evaluate, visualize, and predict future prices.

## 📊 Example Output
- RMSE: ~2.45
- R² Score: ~0.95
- Plot comparing actual vs predicted prices:


## 📌 Future Improvements
- Add LSTM or GRU for sequential prediction.

- Include more technical indicators (RSI, MACD, Bollinger Bands).

- Deploy as a web app using Streamlit or Flask.

- Predict multiple days ahead instead of just next-day price.

## ⚡ Dependencies
- Python 3.10
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- yfinance

## 📄 License
This project is licensed under the Apache License 2.0.

