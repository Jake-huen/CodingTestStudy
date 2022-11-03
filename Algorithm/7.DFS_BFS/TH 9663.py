# 퀸 N개를 서로 공격할 수 없게 놓는 문제
def check(x):
    for i in range(x):
        if row[x]==row[i]:#같은 라인에 있는 경우
            return False
        if abs(i-x)==abs(row[i]-row[x]):#대각선에 있는 경우
            return False
    return True
def dfs(x):
    global answer
    if x==n:
        answer+=1
    else:
        for i in range(n):
            row[x]=i
            if check(x):
                dfs(x+1)
n = int(input())
row = [0] * n
answer = 0
dfs(0)
print(answer)