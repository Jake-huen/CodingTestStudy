from collections import deque

n, k, s = map(int, input().split())  # 아파트 단지 수, 통학버스 정원, 학교 위치
apart_left = []
apart_right = []

for _ in range(n):
    loc, stud = list(map(int, input().split()))  # 아파트 위치, 학생 수
    if loc < s:  # 왼쪽
        apart_left.append([s - loc, stud])
    else:
        apart_right.append([loc - s, stud])
"""
통학버스 -> 학교에서 출발, 학생 태우고, 학교 돌아옴
정원 초과해서 학생 받을 수 없음

학생 수, 거리
"""
apart_left = sorted(deque(apart_left))  # 학교에서 제일 먼곳부터 정렬
apart_right = sorted(deque(apart_right))
# print(apart_left)
# print(apart_right)
max_dist = 0
ans = 0
cur = k

while apart_left:
    dist, num = apart_left.pop()
    max_dist = max(max_dist, dist)
    if cur < num:  # 정원보다 사람이 많을 때
        ans += max_dist * 2  # 현재 거리 왔다갔다
        apart_left.append([dist, num - cur])
        max_dist = 0
        cur = k  # 왔다갔다 했으니까 정원 다시 복구
    else:
        cur -= num  # 학생 태우기
ans += max_dist * 2
max_dist = 0
cur = k

while apart_right:
    dist, num = apart_right.pop()
    max_dist = max(max_dist, dist)
    if cur < num:  # 정원보다 사람이 많을 때
        ans += max_dist * 2  # 현재 거리 왔다갔다
        apart_right.append([dist, num - cur])  # pop으로 뺀거 남은 애들만 다시 집어넣기
        max_dist = 0
        cur = k
    else:
        cur -= num  # 학생 태우기
# print("ans right", ans)
ans += max_dist * 2

print(ans)
