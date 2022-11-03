import sys
sys.stdin.readline

n=int(input())
k=int(input())
#어떤 수보다 작은 자연수의 곱(i*j)이 몇 개인지 알아낼 것이다.
#A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
a=[[0 for _ in range(n+1)]for _ in range(n+1)]
b=[]
for i in range(n+1):
    for j in range(n+1):
        a[i][j]=i*j
        if a[i][j]!=0:
            b.append(a[i][j])
b.sort()
print(b[k-1])

