n, k = map(int, input().split())
feed = list(map(int, input().split()))
"""
먹냐, 안먹냐 + 현재 만족도 상태
"""
dp = [0] * n  # dp[i]: i번쨰 까지의 최대 탈피 에너지
lmax, ans = 0, 0  # lmax : # 애벌레가 먹기 시작하는 구간에서 지금까지 얻었던 최대 탈피 에너지
tmp = 0  # 현재 만족도
left, right = 0, 0  # 투 포인터
while True:
    if tmp >= k:
        if left == 0:
            lmax = 0
        else:
            lmax = max(lmax, dp[left - 1])
        dp[right - 1] = max(dp[right - 1], lmax + tmp - k)
        tmp -= feed[left]
        left += 1
    elif right == n:
        break
    else:
        tmp += feed[right]
        right += 1
for i in range(n):
    ans = max(ans, dp[i])
print(ans)
