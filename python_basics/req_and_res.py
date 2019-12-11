import requests

response  = requests.get('https://www.naver.com').text
 # get은 가져와라 라는 의미 #.text를 추가했음
print(response)