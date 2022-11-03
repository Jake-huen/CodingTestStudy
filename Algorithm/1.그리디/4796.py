answers=[]
while True:
    l,p,v = map(int,input().split())
#연속하는 p일 중, l일 동안만 사용
    if l==0 and p==0 and v==0:
        break
    answer=0
    answer+=v//p*l
    if v%p<l:
        answer+=v%p
    else:
        answer+=l
    answers.append(answer)

for i in range(len(answers)):
    print("Case "+str(i+1)+": "+str(answers[i]))