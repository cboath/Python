import requests
from pprint import pprint
import time
 
# API KEY
API_key = "ee6996823d80627ed711820001bf8d62"
kconst = 273.15
kmultiplier = 1.8
 
# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# This will ask the user to enter city ID
#city_name = input("Enter a city name : ")
city_name = 'St Louis'

# This is final url. This is concatenation of base_url, API_key and city_id
Final_url = base_url + "appid=" + API_key + "&q=" + city_name
 
# this variable contain the JSON data which the API returns
weather_data = requests.get(Final_url).json()

# Temp Conversion
currTemp = weather_data['main']['temp']
tempInF = kmultiplier * (currTemp - kconst) + 32
tempInC = currTemp - kconst# Time conversion
sunrise = time.strftime("%H:%M:%S", time.localtime(weather_data['sys']['sunrise']))
sunset = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(weather_data['sys']['sunset'])) 

# JSON data is difficult to visualize, so you need to pretty print
print('The temp is currently', round(currTemp, 2), 'Kelvin')
print('The temp is currently', round(tempInF, 2), 'Fahrenheit')
print('The temp is currently', round(tempInC, 2), 'Celcius')
print('The sun rose at', sunrise)
print('The sun set at', sunset)
#pprint(weather_data)
