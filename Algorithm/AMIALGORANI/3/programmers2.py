def solution(n, computers):
    answer = 0
    visited = [False]*(n+1)
    def bfs(x):
        for i in range(n):
            if not visited[computers[x][i]]:
                visited[computers[x][i]] = True
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i)
            answer+=1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
