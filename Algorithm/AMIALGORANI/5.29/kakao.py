def solution(alp, cop, problems):
    target_alp = 0
    target_cop = 0
    a = 0
    b = 0
    for x, y, z, w, v in problems:
        target_alp = max(target_alp, x)
        target_cop = max(target_cop, y)
        a = max(a, z)
        b = max(b, w)
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    dp = [[i + j - alp - cop for i in range(target_cop + b + 1)] for j in range(target_alp + a+1)]
    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            if i + 1 <= target_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= target_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for problem in problems:  # 현재 상태에서 풀 수 있는 문제들 추가
                if problem[0] <= i and problem[1] <= j:
                    dp[i + problem[2]][j + problem[3]] = min(dp[i][j] + problem[4],
                                                             dp[i][j] + problem[2] + problem[3],
                                                             dp[i + problem[2]][j + problem[3]])
                    dp[i][j + problem[3]] = min(dp[i][j] + problem[4],
                                                dp[i][j] + problem[3],
                                                dp[i][j + problem[3]])
                    dp[i + problem[2]][j] = min(dp[i][j] + problem[4],
                                                dp[i][j] + problem[2],
                                                dp[i + problem[2]][j])
    answer = dp[target_alp][target_cop]
    for i in range(target_alp, target_alp + a+1):
        for j in range(target_cop, target_cop + b+1):
            answer = min(dp[i][j], answer)
    return answer


# print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
# print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
# print(solution(0, 0, [[0, 0, 1, 1, 1], [150, 150, 1, 1, 100]]))
# print(solution(0, 0, [[4, 3, 1, 1, 100], [0, 0, 2, 2, 1]]))
# print(solution(1, 1, [[0, 2, 1, 1, 100]]))
print(solution(0, 0, [[0, 0, 30, 2, 1], [150, 150, 30, 30, 100]]))
