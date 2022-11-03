# N명의 사람들 매일 아침 한 줄
# N명의 사람, 키는 1부터 N
n = int(input()) # 사람의 수
remember = list(map(int,input().split()))
ans=[0]*(n)
for i in range(n):
    bigger = 0 #자기보다 큰사람이 있는 경우
    for j in range(n):
        if ans[j]==0 and bigger==remember[i]:
            ans[j]=i+1
            break
        elif ans[j]==0:
            bigger+=1
for a in ans:
    print(a,end=' ')