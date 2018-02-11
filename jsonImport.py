import urllib.request, json

with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=demo")
    data = json.loads(url.read().decode())
    print(data)