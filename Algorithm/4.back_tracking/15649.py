#1부터 n까지 자연수 중에서 중복 없이 m개를 고름
"""
백트랙킹은 DFS의 방식을 기반으로, 불필요한 경우를 배제하며 원하는 해답에 도달할 때까지
탐색하는 전략
숫자를 선택하는 경우의 수로 이루어진 트리
반복적으로 숫자를 선택해 m개까지 골라 수열을 완성해야됨
해당 경우의 수를 스택에 추가하고, 동작이 끝난 후에는 다시 스택에서 빼내는 작업
"""
n,m = map(int,input().split())
visited=[False]*(n)
arr=[]
def dfs(cnt):
    if cnt==m:
        print(*arr)
        return
    for i in range(0,n):
        if visited[i]:
            continue
        visited[i]=True
        arr.append(i+1)
        dfs(cnt+1)
        arr.pop()
        print(arr)
        print(visited)
        visited[i]=False
dfs(0)