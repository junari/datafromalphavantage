import pandas as pd
import pandas_ta as ta


# STEP 1: RETRIEVE DATA AND STORE AS CSV
# get data from alpha vantage server
from alpha_vantage.timeseries import TimeSeries
API_key = input("Key in your API key: ")
# input the api key here get the free api key from alpha vantage website
ts = TimeSeries(key=API_key, output_format='pandas')
counter_name = input("what is stock counter symbol (e.g. AAPL, TSLA, IBM): ")
# input counter symbol
data = ts.get_intraday(symbol=counter_name, interval='5min', month='2024-06', outputsize='full')  # savedasionqdatatuple.txt
print(data)
print(type(data))

# store stock data without meta data info
data1 = data[0]
data1.columns  # columns info

# sort data from oldest to newest
data1 = data1.sort_values(by='date')

print(type(data1))  # check data type/class

# save dataframe as csv so that dont have to keep retrieving from server
data1.to_csv('202406_' + counter_name + '.csv')  # save dataframe to csv, dont put index=False, will remove date

# read same data from csv file instead of reading from server
data2 = pd.read_csv('202406_' + counter_name +'.csv')
#data2 = pd.read_csv('202406_AFRM.csv')
# check data type is the same before and after retrieving from csv file
print(type(data1))
print(type(data2))


# STEP 2: CLEAN AND CREATE NEW COLUMNS/ATTRIBUTES FOR ANALYSIS
# create column for rsi, macd, or get macd data and join table
data2['RSI'] = ta.rsi(close=data2['4. close'], length=10)
macd_df = ta.macd(close=data2['4. close'])

# combine main dataframe with macd dataframe
data3 = pd.concat([data2, macd_df], axis=1)

# STEP 3: ANALYZE DATA

# STEP 4: test


