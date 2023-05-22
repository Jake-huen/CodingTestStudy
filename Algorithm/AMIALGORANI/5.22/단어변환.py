from collections import deque


def isCango(start, end):
    cnt = 0
    for i in range(len(start)):
        if start[i] != end[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = [False for i in range(len(words))]
    while q:
        start, cnt = q.popleft()
        if start == target:
            return cnt
        else:
            for i in range(len(words)):
                if not visited[i]:
                    if isCango(start, words[i]):
                        q.append((words[i], cnt + 1))
                        visited[i] = True


# print(isCango("hit", "hot"))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
