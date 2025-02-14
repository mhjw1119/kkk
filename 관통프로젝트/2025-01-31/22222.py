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

# print(dict_keys)

########################데이터를 받아서 json으로 변환 후 해당 값이 딕셔너리로 되어있는것을 확인
###그래서 for문을 이용해서 첫번째부터 마지막 요소의 key값을 dict_keys라는 리스트에 넣어서 출력함
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

#####################################c단계 구현 
sort_dict_korea = {}

def return_dict_korea(info) :
    for i in info :
        if i == "main" :
            sort_dict_korea['기본'] = {}

            for x in info[i] :
                if x == 'feels_like' :
                    sort_dict_korea['기본']["체감온도"] = info[i][x]
                if x == 'humidity' :
                    sort_dict_korea['기본']["습도"] = info[i][x]
                if x == 'pressure' :
                    sort_dict_korea['기본']["기압"] = info[i][x]
                if x == 'temp' :
                    sort_dict_korea['기본']["온도"] = info[i][x]
                if x == 'temp_max' :
                    sort_dict_korea['기본']["최고온도"] = info[i][x]
                if x == 'temp_min' :
                    sort_dict_korea['기본']["최저온도"] = info[i][x]
                if x == 'description' :
                    sort_dict_korea['기본']["요약"] = info[i][x]
                if x == 'icon' :
                    sort_dict_korea['기본']["아이콘"] = info[i][x]
                if x == 'main' :
                    sort_dict_korea['기본']["핵심"] = info[i][x]
                if x == 'id' :
                    sort_dict_korea['기본']["식별자"] = info[i][x]
                if x == 'sea_level' :
                    sort_dict_korea['기본']["해수면"] = info[i][x]
                if x == 'grnd_level' :
                    sort_dict_korea['기본']["육지"] = info[i][x]
            
        elif i == "weather" :
            sort_dict_korea['날씨'] = {}

            for y in info[i][0] :
                if y == 'feels_like' :
                    sort_dict_korea['날씨']["체감온도"] = info[i][0][y]
                if y == 'humidity' :
                    sort_dict_korea['날씨']["습도"] = info[i][0][y]
                if y == 'pressure' :
                    sort_dict_korea['날씨']["기압"] = info[i][0][y]
                if y == 'temp' :
                    sort_dict_korea['날씨']["온도"] = info[i][0][y]
                if y == 'temp_max' :
                    sort_dict_korea['날씨']["최고온도"] = info[i][0][y]
                if y == 'temp_min' :
                    sort_dict_korea['날씨']["최저온도"] = info[i][0][y]
                if y == 'description' :
                    sort_dict_korea['날씨']["요약"] = info[i][0][y]
                if y == 'icon' :
                    sort_dict_korea['날씨']["아이콘"] = info[i][0][y]
                if y == 'main' :
                    sort_dict_korea['날씨']["핵심"] = info[i][0][y]
                if y == 'id' :
                    sort_dict_korea['날씨']["식별자"] = info[i][0][y]
                if y == 'sea_level' :
                    sort_dict_korea['날씨']["해수면"] = info[i][0][y]
                if y == 'grnd_level' :
                    sort_dict_korea['날씨']["육지"] = info[i][0][y]
        else :
            pass
    return sort_dict_korea
# return_dict_korea(data)
print(return_dict_korea(data))

# print(data["weather"][0])

########################################데이터 가공 완료