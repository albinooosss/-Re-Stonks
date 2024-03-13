from adaptive_filter import AdaptiveFilter
from database.parser import *
from database.Columns_Into_List import columns_into_list
from simple_predict import Simple_Predict
import matplotlib.pyplot as plt
from stock_names import stock_names

stock_name = 'PAYX'
data = columns_into_list(get_stock_data(stock_name))
N = 10000
for i in stock_names[:10]:
    data = columns_into_list(get_stock_data(i))
    filter = AdaptiveFilter(data, N)
    simple = Simple_Predict(data)
    filter.adjustment()


    filter.get_pr_err()
    simple.get_errors()