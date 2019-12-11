### python_basics

- visual studio code 와 gitbash 이용한 파이썬

  > ```shell
  > $ pip install requests 
  > # pip는 파이썬으로 작성된 패키지 소프트웨어를 설치 · 관리하는 패키지 관리 시스템
  > $ pip list # requests 확인 가능
  > $ ls
  > $ python req_and_res.py
  > $ pip install bs4
  > $ python kospi.py
  > $ python usd.py
  > ```

- python_basics 폴더 새롭게 생성

  ```shell
  $ cd~
  $ cd TIL/python_basics
  $ git clone https://github.com/edueric-hphk/python_warmup.git
  $ ls
  $ cd python_warmup/
  $ ls -a
  #./  ../  .git/  q1.py  q2.py  q3.py  q4.py  q5.py
  # .git이 들어가있으면 안됌
  $ rm -rf .git
  $ ls -a
  ```

- 새로운 python_warmup 파일에 업로드

  > ```shell
  > $ git status
  > $ git log
  > $ git remote add origin https://github.com/hyunjeong-shin/python_warmup.git
  > $ git remote -v
  > $ git status
  > $ git add . # 파일 여러 개 한꺼번에 추가
  > $ git commit -m "Add q1-5"
  > $ git push origin master
  > ```
  >
  > 