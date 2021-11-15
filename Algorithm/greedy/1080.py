#0과 1로만 이루어진 행렬 A,B A->B로 바꾸는데 필요한 연산 횟수의 최솟값
n,m=map(int,input().split())
a=[]
b=[]
def reverse(x):
    for i in range(3):
        for j in range(3):
            if x[i][j]==0:
                x[i][j]=1
            elif x[i][j]==1:
                x[i][j]=0
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
