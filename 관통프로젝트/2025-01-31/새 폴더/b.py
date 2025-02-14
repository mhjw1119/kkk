import requests


lat = 37.5
lon = 126.97

APIkey = f'cf52b4e5b56bd21cec5c44ba8adc8cbf'
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}'

data = requests.get(URL).json()

#################################데이터 추출 key 값 구현
sort_dict = {}
def return_dict(info) :
    for i in info :
        # print(i)
        if i == "main" or i == "weather" :
            # sort_dict['main'] = i['main']
            # print(info[i])
            # sort_dict.append(info[i])
            sort_dict[i] = info[i]
        else :
            pass
    return sort_dict

print(return_dict(data))