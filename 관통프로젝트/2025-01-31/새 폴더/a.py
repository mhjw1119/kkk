import requests


lat = 37.5
lon = 126.97

APIkey = f'cf52b4e5b56bd21cec5c44ba8adc8cbf'
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}'

data = requests.get(URL).json()

#################################데이터 추출 key 값 구현현
dict_keys = []

for i in data :
    dict_keys.append(i)