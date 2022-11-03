a,b=map(int,input().split())
# 소수의 n제곱 꼴일때 -> 거의 소수
flag=[True]*(int(b**0.5)+1)
flag[1]=False
for i in range(2,int(b**0.5)+1):
    if i*i>int(b**0.5)+1:
        break
    if not flag:
        continue
    for j in range(i*i,int(b**0.5)+1,i):
        flag[j]=False
answer=0
for i in range(1,len(flag)):
    if flag[i]:
        j=i*i
        while True:
            if j<a:
                j*=i
                continue
            if j>b:
                break
            j*=i
            answer+=1
print(answer)