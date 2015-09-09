import os
from time import time
import numpy as np
import pandas as pd

quandl_tickers = [filename[:-4] for filename in os.listdir('/Users/excalibur/Dropbox/datasets/quandl_data/') if filename != '.DS_Store']
print quandl_tickers

goog_tickers = [filename[:-4] for filename in os.listdir('/Users/excalibur/Dropbox/datasets/goog_data/') if filename != '.DS_Store']
print goog_tickers

tickers = []
for quandl_ticker in quandl_tickers:
    if quandl_ticker in goog_tickers:
        tickers.append(quandl_ticker)
print tickers
print len(tickers)

def convert_data_to_df(ticker):
    df = pd.read_csv("/Users/excalibur/Dropbox/datasets/quandl_data/{}.csv".format(ticker))
    df = df.drop('Adjusted Close', axis=1)

    df['50dravg'] = pd.rolling_mean(df['Close'], window=50)
    df['200dravg'] = pd.rolling_mean(df['Close'], window=200)

    df['OC%'] = (df['Close'] / df['Open']) - 1
    df['HL%'] = (df['High'] / df['Low']) - 1
    df['OH%'] = (df['High'] / df['Open']) - 1
    
    df['LastOpen'] = df['Open'].shift(1)
    df['LastHigh'] = df['High'].shift(1)
    df['LastLow'] = df['Low'].shift(1)
    df['LastClose'] = df['Close'].shift(1)
    df['LastVolume'] = df['Volume'].shift(1)
    df['LastOC%'] = df['OC%'].shift(1)
    df['LastHL%'] = df['HL%'].shift(1)
    df['LastOH%'] = df['OH%'].shift(1)

    df['ticker'] = ticker

    df['label'] = df['OH%'].shift(-1)
    
    return df.copy()

stock_df = pd.DataFrame()
for ticker in tickers:
    if stock_df.empty:
        stock_df = convert_data_to_df(ticker)
    else:
        stock_df = stock_df.append(convert_data_to_df(ticker))

stock_df = stock_df.replace([np.inf, -np.inf], np.nan)
stock_df = stock_df.dropna()
stock_df = stock_df[stock_df['date'] > '2010-01-01'] # get more recent data
stock_df = stock_df[(stock_df['Open'] > 1.0) & (stock_df['Open'] < 9.0)] # get stocks over 1.0 and less than 9.0
print stock_df.shape
stock_df.to_csv('quandl.csv', index=False)
stock_df.head()
