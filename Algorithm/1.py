T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    scores = list(map(int, input().split()))
    dp = [0] * (max(scores) + 1)
    for score in scores:
        dp[score] += 1
    for i in range(len(dp)):
        if dp[i] > 0:
            start = i + 1
            break
    for i in range(len(dp) - 1, -1, -1):
        if dp[i] > 0:
            end = i
            break
    temp = 0
    answer = 0
    for i in range(start, end):
        if dp[i] > 0:
            temp += dp[i]
            if temp > b:
                break
            else:
                answer += dp[i]
    print("#" + str(test_case), answer)

"""
3
6 1 3
4 3 2 3 2 1
6 3 4
1 2 3 4 5 6
6 1 4
10 10 9 10 3 3
"""
