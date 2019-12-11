import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(response, 'html.parser')
#print(type(response))
#print(type(soup))

kospi =soup.select_one("#KOSPI_now").text
print(kospi)


