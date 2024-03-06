# importing module
from pandas import *

import analysis_model.adaptive_filter

data = read_csv("new_sp500.csv")


def combine_columns_into_list(data, column_names):
    combined_list = [list(row) for row in zip(*(data[column].tolist() for column in column_names))]
    return combined_list


column_names = ['High', 'Low', 'Open', 'Close', 'Volume']
combined_data = combine_columns_into_list(data, column_names)
# print(combined_data[:10])

# print(combined_data[0])

# ex = analysis_model.adaptive_filter.AdaptiveFilter(combined_data,11)
# print(ex.adjustment())