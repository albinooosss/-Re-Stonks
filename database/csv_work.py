import pandas as pd

# Чтение csv файла
df = pd.read_csv('sp500_stocks.csv')

# Преобразование колонки 'Date' в формат даты
df['Date'] = pd.to_datetime(df['Date'])

# Фильтрация данных, оставляя только те, которые после 2020 года
filtered_df = df[df['Date'].dt.year >= 2021]

# Сохранение отфильтрованных данных в новый csv файл
filtered_df.to_csv('new_sp500.csv', index=False)

