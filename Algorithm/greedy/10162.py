t=int(input())
#a b c : 300초 60초 10초
#최소횟수
oven = [300,60,10]
answer=[]
for i in oven:
    answer.append(t//i)
    t=t%i
if t==0:
    for i in range(3):
        print(answer[i],end=' ')
else:
    print(-1)