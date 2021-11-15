#0과 1로만 이루어진 행렬 A,B A->B로 바꾸는데 필요한 연산 횟수의 최솟값
n,m=map(int,input().split())
a=[]
b=[]
cnt=0
def reverse(arr,x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if arr[i][j]==0:
                arr[i][j]=1
            elif arr[i][j]==1:
                arr[i][j]=0
def same(x,y):
    for i in range(n):
        for j in range(m):
            if x[i][j]!=y[i][j]:
                return False
    return True
for _ in range(n):
    a.append(list(map(int,input())))
for _ in range(n):
    b.append(list(map(int,input())))
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            reverse(a,i,j)
            cnt+=1
        else:
            continue
if same(a,b):
    print(cnt)
else:
    print(-1)