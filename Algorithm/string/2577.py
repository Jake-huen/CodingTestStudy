num=[]
for i in range(3):
    num.append(int(input()))
answer = num[0]*num[1]*num[2]

answer=str(answer)
cnt=[0]*10
for i in range(len(answer)):
    s=int(answer[i])
    cnt[s]+=1
for i in range(10):
    print(cnt[i])