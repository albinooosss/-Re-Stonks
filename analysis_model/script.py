from adaptive_filter import AdaptiveFilter
from database.parser import *
from database.Columns_Into_List import columns_into_list


def apply(company_name):
    data = columns_into_list(get_stock_data(company_name))
    N = 50
    filter = AdaptiveFilter(data, N)
    filter.adjustment(1)
    return filter.apply(sum(data[-1]) / len(data[-1]), sum(data[-2]) / len(data[-2]))
