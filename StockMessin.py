from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='D3F0HVMFLMPCVLRN', output_format='pandas')

with open('list.txt', 'r') as stocks:
    for x in stocks:
        print('The stock is', x)
        data, meta_data = ts.get_intraday(symbol=x.rstrip(), interval='1min', outputsize='compact')

        singleVal = data['4. close'].tail(1).to_string()

        a, b, c = singleVal.partition('    ')
        g = float(c)

        h= g*2

        print(h)
