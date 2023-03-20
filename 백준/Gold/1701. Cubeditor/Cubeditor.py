n = list(input())
ans = 0


def kmp(pattern):
    graph = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]: #서로 문자가 다를때 앞에까지로 돌아가야 함.
            j = graph[j - 1]
        if pattern[i] == pattern[j]: # 같을때는 같은 개수 계속 업데이트
            j += 1
            graph[i] = j
    return graph


for i in range(len(n)):
    ans = max(ans, max(kmp(n[i:])))
print(ans)
