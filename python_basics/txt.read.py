
with open('mulcam.txt','r') as text:
    lines = text.readlines() #읽어왔음
    lines.sort(reverse=True)
    for line in lines:
        print(line.strip())


#lines.reverse()

with open('mulcam.txt','w') as text:
    for line in lines:
        f.write(line)