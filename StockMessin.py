from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='', output_format='pandas')

with open('list.txt', 'r') as stocks:
    for x in stocks:
        print('The stock is', x)
        data, meta_data = ts.get_intraday(symbol=x.rstrip(), interval='1min', outputsize='compact')
 
        lastVal = data['4. close'].tail(1).to_string()

        data.describe()

        singleVal = data['4. close'].tail(1).to_string()
        print(singleVal)
