import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
# парсер данных по выбранной пользователем акции за неделю сохраняет данные
# в csv файл с этой акцией в названии. в последней строке файла во всех столбцах,
# кроме Volume (равен 0) содержтся цена акции на текущй момент времени
# тестила программу на акции 'MMM', данные успешно сохранились в MMM_data.csv

# stock_name='MMM'


def get_current_stock_price(stock_name):
	stock = yf.Ticker(stock_name)
	data = stock.history(period='1d')
	current_price = data['Close'].iloc[-1]

	return current_price


def get_stock_data(stock_name):
	data = pd.DataFrame()
	start_date = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
	end_date = datetime.today().strftime('%Y-%m-%d')

	stock_data = yf.download(stock_name, start=start_date, end=end_date)
	stock_data['Symbol'] = stock_name
	data = pd.concat([data, stock_data], axis=0)

	data = data.reset_index()[['Date', 'Symbol', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']]

	current_price = get_current_stock_price(stock_name)
	current_time = datetime.now().strftime('%H:%M:%S')
	current_data = pd.DataFrame({'Date': [datetime.today().strftime('%Y-%m-%d') + ' ' + current_time],
								 'Symbol': stock_name,
								 'Adj Close': [current_price],
								 'Close': [current_price],
								 'High': [current_price],
								 'Low': [current_price],
								 'Open': [current_price],
								 'Volume': [0]})  # Устанавливаем объем как 0 для текущей цены

	data = pd.concat([data, current_data], axis=0)

	# Сохраняем данные в файл CSV
	data.to_csv(f"{stock_name}_data.csv", index=False)

# get_stock_data(stock_name)

