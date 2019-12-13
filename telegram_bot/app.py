from flask import Flask
from flask import request
from flask import render_template
from decouple import config
import requests
import random

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
# chat_id = config('CHAT_ID')
token = '1019040169:AAHbYeK-eTxkiNIVes4PMNmpsdQGvO6BTpI'
app_url = f'https://api.telegram.org/bot{token}'

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET') #  환경변수 가져옴


# @app.route(f'/{token}',methods=['POST']) # 이 주소로 포스트 요청만 보냄
# def telegram():
#     # 1. request print 해보기
#     from_telegram = request.get_json()

#     chat_id = from_telegram.get('message').get('from').get('id')
#     text = from_telegram.get('message').get('text')


#     if text == '로또'
#           reply = random.sample(range(1,46),6)
#           
#     else:
#           reply = text

#     requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')


#     return '' , 200 #200은 응답true값


#     # print(request.get_json())


# '/로또 라고 입력을 하면, 로또 번호 6자리를 뽑아서 보내주기
@app.route(f'/{token}',methods=['POST'])
def telegram():
    from_telegram = request.get_json()
    chat_id = from_telegram.get('message').get('from').get('id')
    text = from_telegram.get('message').get('text')
    if from_telegram.get('message').get('photo') is not None:

        #1. 우선 파일의 아이디 값을 가져온다
        file_id = from_telegram.get('message').get('photo')[-1].get('file_id')
        print(from_telegram)

        #2. 가져온 파일 아이디로 실제 파일을 가져온다.
        file_res = requests.get(f'{app_url}/getfile?file_id={file_id}')

        #3. file path를 뽑아내서 지정
        file_path = file_res.json().get('result').get('file_path')

        #4. 최종적으로 해당 파일의 경로를 찾아서 저장
        file_url = f'https://api.telegram.org/file/bot{token}/{file_path}'
        # print(file_url)

        # 5. 사진(파일)이 있는 주소로 요청을 보내서 가져오자
        real_file_res = requests.get(file_url, stream=True)

        headers = {
            'X-Naver-Client-Id' : naver_client_id,
            'X-Naver-Client-Secret' : naver_client_secret
        }
        clova_res = requests.post('https://openapi.naver.com/v1/vision/celebrity' ,headers=headers, 
        files={'image':real_file_res.raw.read()})
        #print(clova_res.json())
        #닮은 유명인의 수가 있을 경우
        if clova_res.json().get('info').get('faceCount'):
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            reply = f"{celebrity.get('value')} - {celebrity.get('confidence')*100}%"
        else:
            reply = '인식된 사람이 없습니다'

        #reply="인식하지못합니다"
        # 클로바 코드 요기에 작성
    else:
        # text가 왔을 때 실행
        if text == "로또":
            reply= random.sample(range(1,46),6)
        if text[0:2] == '번역':  # 번역할 문장 입력
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {
            'source' : 'en',
            'target' : 'ko',
            'text' : text[2:]

            }

            data = {
            'source' : 'ko',
            'target' : 'en',
            'text' : text[2:]

            }
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            papago_res = requests.post(papago_url, data=data, headers=headers)

            papago_res = papago_res.json()
            reply = papago_res.get("message").get("result").get("translatedText")
        else:
            reply = text
    print(from_telegram)        
    requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={reply}')
    return '' , 200 #200은 응답true값

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    message = request.args.get('message')
    message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return '메세지 전송 완료 했어요^_^'



if __name__ == '__main__':
    app.run(debug=True)