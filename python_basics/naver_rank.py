import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text
soup = BeautifulSoup(response, 'html.parser')

rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul span.ah_k')
#for naver in rank:
    #print(naver.text)


with open('naver.txt','w', encoding = 'utf-8') as f:
    f.write('네이버 검색어 순쉬 \n')
    for i, naver in enumerate(rank):
        f.write(f'{i+1}. {naver.text} \n')

