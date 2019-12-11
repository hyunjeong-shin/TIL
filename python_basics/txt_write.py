f = open('mulcam.txt','w')
for i in range(10):
    f.write(f"This is line {i}. \n")
f.close()
# 파일을 열고 닫아줘야함

with open('mulcam2.txt', 'w') as file:
    for i in range(10):
        file.write(f"This is line {i}. \n")

# with는 알아서 파일을 닫아준다


with open('mulcam.txt', 'r') as f: #f는 mulcam파일에 대한 변수명
    lines = f.readlines()
    for line in lines:
         print(line.strip())

with open('mulcam.txt','r') as f:
    lines.sort(reverse=True)
    lines = f.readlines()
    for line in lines:
        print(line.strip())
