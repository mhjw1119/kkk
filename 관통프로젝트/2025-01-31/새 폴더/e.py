import requests


APIkey = f'cf52b4e5b56bd21cec5c44ba8adc8cbf'
URL=f'https://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid={APIkey}&units=metric'


data = requests.get(URL).json()
# 5일 후 날짜 (예: 2025-02-05)
target_date = "2025-02-05"

# 특정 날짜 데이터 필터링
forecast_data = [
    entry for entry in data["list"] if target_date in entry["dt_txt"]
]

# 결과 출력
for entry in forecast_data:
    print(f"시간: {entry['dt_txt']}, 온도: {entry['main']['temp']}°C, 날씨: {entry['weather'][0]['description']}")