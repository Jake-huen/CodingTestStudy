"""투포인터를 이용해 만족도(tmp)가 K 이상이기 까지 arr[right]를 더하면서 right를 증가시킨다.
현재 만족도가 K 이상일 경우, 탈피에너지를 갱신한다.

"""
n, k = map(int, input().split())
feed = list(map(int, input().split()))

dp = [0] * n  # dp[i]: i번쨰 까지의 최대 탈피 에너지  
lmax, ans = 0, 0  # lmax : 애벌레가 먹기 시작하는 구간에서 지금까지 얻었던 최대 탈피 에너지  
tmp = 0  # 현재 만족도  
left, right = 0, 0  # 투 포인터  
while True:
    if tmp >= k:  # k를 넘겼으면 탈피해야함
        if left == 0:
            lmax = 0
        else:
            lmax = max(lmax, dp[left - 1])
            # 지금까지 얻었던 탈피 에너지 + 현재 위치에서 얻은 탈피 에너지
        dp[right - 1] = max(dp[right - 1], lmax + tmp - k)
        # 현재 만족도 감소  
        tmp -= feed[left]
        left += 1
    elif right == n:  # 마지막일 때
        break
    else:
        tmp += feed[right]  # 현재 만족도를 올린다음
        right += 1  # 오른쪽 포인터를 하나 옮기기
for i in range(n):
    ans = max(ans, dp[i])
print(ans)
