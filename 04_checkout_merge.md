## checkout & merge

> ```shell
> $ rm -rf .git  #(master)빠져나오기
> 
> $ mkdir problems
> $ cd problems
> $ code .  # Visual studio code 열림
> 
> # Visual studio code 에서 a.txt 파일과 b.txt 파일 생성
> 
> $ git init
> $ git add a.txt
> $ git add b.txt
> 
> $ git rm --cached a.txt # add 된 것 되돌리는 법
> $ git status # a.txt는 Untracked file된 것을 확인 가능
> $ git add a.txt
> $ git rm --cached b.txt
> $ git status  # b.txt 가 untracked file 된 것을 확인 가능
> 
> $ git commit -m "Add b.txt" 
> # a를 add 해야하는데 b로 commit 실수 했을 경우
> $ git log --oneline
> # 89cc8eb (HEAD -> master) Add b.txt 
> 
> $ git commit --amend
> # 입력 할 경우 이상한 창으로 이동
> # 수정하고 싶은 부분에 i 누르고 b를 a로 수정 후 ESC
> # :wq 입력 후 종료
> # commit b 되돌린다 > commit a 로 수정 완료
> 
> $ git reset --hard c904587
> # HEAD가 C904587 당시로 이동
> 
> $ git checkout c904587
> # c904587로 브랜치 이동
> $ git add c.txt
> $ git checkout master # 다시 마스터로..
> 
> ```

## branch

> ```shell
> $ git status
> $ git log --oneline
> # c904587 (HEAD -> master) Add b.txt
> # 84b498e Add a.txt
> $ ls
> ```

- branch 로 현재 있는 세계 파악 가능

> ```shell
> $ git branch
> * master # 현재 내 위치 master
> 
> $ git branch test # test라는 브랜치 추가
> $ git branch
> * master # 아직 위치는 master
>   test
>   
> $ git checkout test # checkout사용하면 branch 이동
> $ git branch -D test # test branch 제거
> 
> $ git checkout -b new 
> # checkout & branch 만들면서 head new로 이동
> ```

### merge

> ```shell
> $ git merge test # 어느 브랜치를 중심으로 합칠 것인지
> # 중심이 되는 브랜치로 이동하는게 핵심
> # 1.ff(first-forward) 2.auto 3.merge-conflict
> 
> $ git log --oneline --graph
> #master branch에 test branch 합쳐진다.
> #*   ca60911 (HEAD -> master) Merge branch 'test'
> #|\
> #| * f77790f (test) Add test.txt (test branch)
> #* | c1a80e5 Add master.txt (master branch)
> #|/
> #* 07c3a8a Add new.txt
> #* c904587 Add b.txt
> #* 84b498e Add a.txt
> 
> $ git diff
> $ git checkout -b feature/data # 이런 형식 나중에 자주 사용
> 
> 
> 
> ```

### conflict

- 내용은 다른데 이름이 같은 폴더를 merge 할 경우 충돌이 일어날 때
  - visual studio code에서 충돌 일어난 것 변경 사항 선택해주기

> ```shell
> $ git merge feature/data
> # both modified:   master.txt
> # master 브랜치와 feature/data 브랜치 master 동일 파일명 충돌
> # visual studio code에서 충돌 변경사항 선택 후
> $ git add master.txt
> $ git commit -m "Resolve merge conflict"
> 
> ```

