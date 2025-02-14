import requests
import pprint
# 하드 코딩하는 변수는 대문자로 쓴다.
URL = 'https://fakestoreapi.com/carts'
# . get(URL) : url 주소에 요청을 보내는 메서드
data = requests.get(URL)
#<Response [200]>
# [200] >> 웹의 응답 코드 (정상적으로 응답이 왔다는 뜻)
#<Response [404]>
# [404] >> 웹의 응답 코드( 알 수 없는 주소로 요청했다.)

print(data)


# .json() : 데이터를 json형태로 변환해주는 메서드
json_data = data.json()
print(json_data)
print(type(json_data))
pprint.pprint(json_data)
cf52b4e5b56bd21cec5c44ba8adc8cbf
