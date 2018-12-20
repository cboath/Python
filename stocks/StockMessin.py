#required_pkgs = ['alpha_vantage', 'pandas']
#installed_pkgs = [pkg.key for pkg in pkg_resources.working_set]

#for package in required_pkgs:
    #if package not in installed_pkgs:
        #print('Installing', package)
        #subprocess.check_call(["python", '-m', 'pip', 'install', package])
        
        
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='D3F0HVMFLMPCVLRN', output_format='pandas')

import sys
import pkg_resources
import pip
import subprocess

with open('list.txt', 'r') as stocks:
    for x in stocks:
        currentSym = x.rstrip()
        print('The stock is {0}'.format(currentSym))
        data, meta_data = ts.get_intraday(symbol=currentSym, interval='1min', outputsize='compact')

        singleVal = data['4. close'].tail(1).to_string()

        a, b, c = singleVal.partition('    ')
        g = float(c)

        print(g)
