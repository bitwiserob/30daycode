import pandas as pd
import numpy as np

from pandas_datareader.data import DataReader
import yfinance as yf

from pandas_datareader import data as pdr

yf.pdr_override()

from datetime import datetime




stocklist = ['AAPL', 'MSFT', 'AMZN', 'GOOG']
names = ['APPLE','MIRCOSOFT','AMAZON' ,'GOOGLE']

for stock in stocklist:
    end = datetime.now()
    start = datetime(end.year - 1, end.month - 1, end.day)
    globals()[stock] = yf.download(stock, start, end)

stock_data = [AAPL, MSFT, AMZN,GOOG]


df = pd.concat(stock_data, axis = 0)
df.to_csv(index=False)



