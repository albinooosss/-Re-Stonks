from adaptive_filter import AdaptiveFilter
from database.parser import *
from database.Columns_Into_List import columns_into_list
from simple_predict import Simple_Predict
import matplotlib.pyplot as plt
from stock_names import stock_names
from random_predict import Random_Predict
from stable_ratio import Stable_Ratio
from avg_predict import Average_Predict


N = 50
for i in stock_names[:10]:
    data = columns_into_list(get_stock_data(i))
    filter = AdaptiveFilter(data, N)
    simple = Simple_Predict(data, 21)
    filter.adjustment(21)
    rand = Random_Predict(data)
    stable = Stable_Ratio(data, 21)
    avg = Average_Predict(data)
    #print(filter.MSE())
    #filter.show_plots()
    #print(simple.MSE())
    #simple.show_plots()
    print('R = ', filter.Coefficient_of_determination(simple))
    #print(rand.MRE())
    #rand.show_plots()
    #print(stable.MRE())
    #stable.show_plots()
    #print(avg.MRE())
    #avg.show_plots()
