# push & pull WORKFLOW

### 처음 시작 (Github > home)

- Git bash 프로그램 시작

  ```shell
  $ pwd  # home 폴더인지 확인
  $ mkdir house # 주소를 house로 
  $ cd house
  ```

- Github 에서 원격 저장소의 주소를 복제

  ```shell
  $ git clone https://github.com/hyunjeong-shin/TIL.git
  $ ls  #list 확인
  ```

- 새로운 파일 추가

  ```shell
  #house bush에서 작동중
  
  $ touch homework.txt
  $ ls  # homework.txt 추가 된 것을 확인 할 수 있다 
  $ git status
  
  $ git add homework.txt
  $ git status # 초록색 글씨로 new file 추가 확인 가능
  $ git commit -m "Add homework.txt"
  ```

- 파일 로그 확인

  ```shell
  $ git log
  $ git log --oneline  # 한 줄로 짧게 확인 가능
  $ git log -1  # 마지막 한 줄만 확인
  ```

- home에서 Github로 다시 push

  ```shell
  $ git push origin master
  $ git status
  ```

  

### multicam에서 확인 (home > Github > multicam)

- Git bash 프로그램 시작

  ```shell
  $ cd TIL
  $ git log
  $ ls
  $ git status # pull 부터 무조건 하지말고 꼭 status 확인
  ```

- pull 로 불러오기

  ```shell
  $ git pull origin master
  $ git log
  $ ls
  $ git status
  ```

- multicam 에서 new 파일 생성 후 Github로 push

  ```shell
  $ touch new.md
  $ git add new.md
  $ git status
  $ git commit -m "Add new.md"
  $ git push origin master
  ```

- home 에서 quiz. txt 생성

  ```shell
  $ touch quiz.txt
  $ git status
  $ git add quiz.txt
  $ git commit -m "Add quiz.txt"
  $ git push origin master
  ```

- multicam 에서 quiz.txt 수정하기

  ```shell
  $ git status # 아무것도 안 떠야 정상
  $ git log # quiz.txt 생성 된 것 확인 가능
  $ git pull origin master #Github에서 불러오기
  $ git add quiz.txt # quiz 추가 후 파일 내용을 수정해봄
  $ cat quiz.txt # cat 이용하여 수정된 내용 확인 가능
  $ git add quiz.txt # 다시 quiz 파일을 붙여 넣어줌
  $ git commit -m "modify quiz.txt"
  $ git push origin master
  ```

### home 에서 다시 확인

```shell
$ git status
$ git pull origin master # 새로 추가된 것 확인 가능
```

