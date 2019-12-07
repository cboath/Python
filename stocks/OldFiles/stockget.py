from alpha_vantage.timeseries import TimeSeries

#print('The stock is', x.rstrip())
def getStock(ticker):
    data, meta_data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='compact')
    
    singleVal = data['4. close'].tail(1).to_string()
    a, b, c = singleVal.partition('    ')
    g = float(c)
    return g
