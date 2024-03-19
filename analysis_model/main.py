from adaptive_filter import AdaptiveFilter
from database.parser import *
from database.Columns_Into_List import columns_into_list
from simple_predict import Simple_Predict
import matplotlib.pyplot as plt
from stock_names import stock_names
from random_predict import Random_Predict
from stable_ratio import Stable_Ratio
from avg_predict import Average_Predict


N = 10
for i in stock_names[:1]:
    data = columns_into_list(get_stock_data(i))[:1000]
    filter = AdaptiveFilter(data, N)
    simple = Simple_Predict(data, 5)
    filter.adjustment(5)
    rand = Random_Predict(data)
    stable = Stable_Ratio(data, 5)
    avg = Average_Predict(data)
    print(filter.MRE())
    filter.show_plots()
    print(simple.MRE())
    simple.show_plots()
    print(rand.MRE())
    rand.show_plots()
    print(stable.MRE())
    stable.show_plots()
    print(avg.MRE())
    avg.show_plots()
