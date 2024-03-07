from pandas import *

# data = read_csv("MMM_data.csv")

def columns_into_list(data):
    column_names = ['High', 'Low', 'Open', 'Close', 'Volume']
    combined_list = [list(row) for row in zip(*(data[column].tolist() for column in column_names))]
    return combined_list


# combined_data = combine_columns_into_list(data)
# print(combined_data[0])
