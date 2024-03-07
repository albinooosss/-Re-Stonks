import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
# парсер данных по выбранной пользователем акции за неделю сохраняет данные
# в csv файл с этой акцией в названии
# тестила программу на акции 'MMM', данные успешно сохранились в MMM_data.csv
# stock_name='MMM'

def get_stock_data(stock_name):
	data = pd.DataFrame()
	start_date = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
	end_date = datetime.today().strftime('%Y-%m-%d')

	stock_data = yf.download(stock_name, start=start_date, end=end_date)
	stock_data['Symbol'] = stock_name
	data = pd.concat([data, stock_data], axis=0)
	data = data.reset_index()[['Date', 'Symbol', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']]

	# Сохраняем данные в файл CSV
	data.to_csv(f"{stock_name}_data.csv", index=False)


# get_stock_data(stock_name)