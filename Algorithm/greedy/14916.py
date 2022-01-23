n = int(input())
# d=[-1]*(n+8)
# d[2]=1
# d[4]=2
# d[5]=1
# d[6]=3
# d[7]=2
# d[8]=4
# for i in range(9,n+1):
#     d[i]=min(d[i-2],d[i-5])+1
# print(d[n])
cnt =0
i=0
while True:
    if n%5==0: #5의 배수이면
        cnt+=n//5
        break
    else:
        n-=2 #5의 배수가 아니면 2를 계속 빼면서 5로 나누어떨어지게
        cnt+=1
    if n<0:
        break
if n<0:
    print(-1)
else:
    print(cnt)