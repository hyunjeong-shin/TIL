from flask import Flask
from flask import request
from flask import render_template
from flask import requests
import random
import requests

app = Flask(__name__) # 서버 이름

@app.route('/') #서버의 길 루트 주소
def hello_world():
    return 'Hello, World!' #return은 요청에 대한 응답

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Hello, {name}!'

@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['마라탕', '마라샹궈', '꿔바로우']
    order = random.sample(menu, people)
    return str(order)

@app.route('/html')
def html():
    return '<h1>안녕하세용</h1>'

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html', name=name , message=message)

@app.route('/writename')
def select():
    return render_template('writename.html')

@app.route('/select')
def select():
    name = request.args.get('name')
    options = ['미모','키','시력','눈','코','입','몸무게']
    order = random.sample(options,2)
    return render_template('select.html', name = name , message1= order[0] , message2 = order[1])

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/vonvon_result')
def vonvon_result():
    name = request.args.get('nickname')
    return


@app.route('/ascii')
def ascii():
    return render_template('/ascii.html')

@app.route('/ascii_result')
def ascii_result():
    # 1. form 태그로 날린 데이터(word)를 받는다
    word = 
    # 2. word를 가지고 ascii_art API 요청 주소로 요청을 보낸다
    result = requests.get(f'http://artii.herouapp.com/make?text={word}')
    # 3. API 응답 결과를 html 파일에 담아서 보여준다.
    return render_template('ascii_result.html', )

if __name__== "__main__":
    app.run(debug=True)  # 이 파일이 직접 실행했을 떄만 실행해라. 불러왔을때는 안됨
