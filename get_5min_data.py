import pandas as pd
import pandas_ta as ta

# get data from alpha vantage server
from alpha_vantage.timeseries import TimeSeries
API_key = '2G54W62Y65RLE31I'
ts = TimeSeries(key=API_key, output_format='pandas')
data = ts.get_intraday('AFRM', interval='5min', month='2024-06', outputsize='full')  # savedasionqdatatuple.txt
print(data)
print(type(data))

# store stock data without meta data info
data1 = data[0]
data1.columns #columns info

# sort data from oldest to newest
data1=data1.sort_values(by='date')

print(type(data1))  # check data type/class

# save dataframe as csv so that dont have to keep retrieving from server
data1.to_csv('202406_AFRM.csv')  # save dataframe to csv, dont put index=False, will remove date

# read same data from csv file instead of reading from server
data2 = pd.read_csv('202406_AFRM.csv')

# check data type is the same before and after retrieving from csv file
print(type(data1))
print(type(data2))

# create column for rsi, macd, or get macd data and join table
data2['RSI'] = ta.rsi(close=data2['4. close'], length=10)
macd_df = ta.macd(close=data2['4. close'])

# combine main dataframe with macd dataframe
data3 = pd.concat([data2, macd_df], axis=1)

# data2=data2.drop(columns=['MACD', 'macd1', 'cad']) #delete columns
