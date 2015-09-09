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
    df = pd.read_csv("/Users/excalibur/Dropbox/datasets/goog_data/{}.csv".format(ticker))

    df = df[(df['time'] == 9.30) | (df['time'] == 10.0)]
    
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    df = df[df['date'] > '2010-01-01'] # get more recent data
    df = df[(df['OPEN'] > 1.0) & (df['OPEN'] < 9.0)] # get stocks over 1.0 and less than 9.0

    df_930 = df[df['time'] == 9.30]
    df_100 = df[df['time'] == 10.0]
    
    df = df_930.merge(df_100, how='inner', on='date')
    
    df['volume_change'] = df['VOLUME_y'] - df['VOLUME_x']
    
    df['volume_change_perc'] = (df['VOLUME_y'] / df['VOLUME_x']) - 1
    
    df['ticker'] = ticker
    
    return df.copy()

stock_df = pd.DataFrame()
for ticker in tickers:
    if stock_df.empty:
        stock_df = convert_data_to_df(ticker)
    else:
        stock_df = stock_df.append(convert_data_to_df(ticker))


print stock_df.shape
stock_df.to_csv('goog.csv', index=False)
stock_df.head()

