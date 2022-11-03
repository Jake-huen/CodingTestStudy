n = int(input())
cow_where=[-1 for _ in range(10)]
answer=0
for i in range(n):
    x,y = map(int,input().split()) # 소의 번호, 소의 위치
    x=x-1
    if cow_where[x]==-1:#위치 처음
        cow_where[x]=y
    elif cow_where[x]==0:
        if y==1: #0에서 1로 건너감
            cow_where[x]=y
            answer+=1
    elif cow_where[x]==1:
        if y==0:
            cow_where[x]=y
            answer+=1
print(answer)
