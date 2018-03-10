from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='compact')
data.describe()
print(data)