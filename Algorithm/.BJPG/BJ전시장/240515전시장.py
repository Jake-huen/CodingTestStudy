"""
직사각형 모양, 높이는 다르지만 폭은 동일
앞에서 봤을 때 보이는 부분이 s이상만 판매가능

판매가능 그림들의 가격의 합이 최대가 되도록
"""
import sys
input = sys.stdin.readline
n, s = map(int, input().split())  # 그림 개수, 판매가능 그림 길이
picture_info = []
for i in range(n):
    h, c = map(int, input().split())  # 높이, 가격
    picture_info.append([h, c])
"""
DP[i] -> i번째 그림까지 봤을 때 최대 값(i번째 사용하든 안하든 상관없음)
DP[i] = max(DP[i-1], DP[j] + cost[i]) 
    여기서 j는 영역 내 최대값
"""
picture_info.sort(key=lambda x: (x[0], -x[1]))  # 높이 낮은 순, 가격 높은 순
# print(picture_info)
dp = [-1000001] * n
prev_max = 0
prev_idx = 0
for i in range(n):
    for j in range(prev_idx, i):
        if picture_info[i][0] - picture_info[j][0] < s:  # 차이가 s보다 작은 경우
            break
        prev_idx = j
        prev_max = max(prev_max, dp[j])
    dp[i] = max(dp[i-1], prev_max + picture_info[i][1])

print(max(dp))
