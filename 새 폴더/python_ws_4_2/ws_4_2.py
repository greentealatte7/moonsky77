# ws_4_2.py
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

#url 반복문
dummy_data = []
for i in range(1,11) :
    url_full = API_URL+str(i)
    response = requests.get(url_full)
    parsed_data = response.json()
    name = parsed_data['name']
    dummy_data.append(name)

print(dummy_data)

#
# # API 요청
# response = requests.get(url_full)


# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])


