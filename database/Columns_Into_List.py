# importing module
from pandas import *

# reading CSV file
data = read_csv("sp500_stocks.csv")

# converting column data to list
date = data['Date'].tolist()
name = data['Symbol'].tolist()
max = data['High'].tolist()
min = data['Low'].tolist()
open = data['Open'].tolist()
close = data['Close'].tolist()

# printing list data
#print('Date:', date)
print('High:', max)