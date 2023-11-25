from itertools import combinations, product


def calculate_probability(dice, A, B, dp):
    a_temp = [dice[i] for i in A]
    a_combinations = list(product(*a_temp))
    # print(a_combinations)
    b_temp = [dice[i] for i in B]
    b_combinations = list(product(*b_temp))
    # print(b_combinations)
    total_combinations = 0
    win_count = 0
    lose_count = 0
    for a_combi in a_combinations:
        for b_combi in b_combinations:
            total_combinations += 1
            if sum(a_combi) > sum(b_combi):
                win_count += 1
            elif sum(a_combi) < sum(b_combi):
                lose_count+=1
    win_probability = win_count / total_combinations
    lose_probability = lose_count / total_combinations
    dp[A] = win_probability
    dp[tuple(B)] = lose_probability
    return win_probability


def solution(dice):
    answer = []
    answer_prob = 0
    num_dice = len(dice)
    num_selected_dice = num_dice // 2
    # 모든 조합을 구해야 함
    temp = [i for i in range(len(dice))]
    combinations_A = list(combinations(temp, num_selected_dice))
    dp = {tuple(combi_A): 0 for combi_A in combinations_A}
    #print(dp)
    for combi_A in combinations_A:
        combi_B = []
        for i in range(len(dice)):
            if i not in combi_A:
                combi_B.append(i)
        if dp[tuple(combi_A)] > 0:
            #print("시간")
            prob = dp[tuple(combi_A)]
            #prob = calculate_probability(dice, combi_A, combi_B, dp)
        else:
            prob = calculate_probability(dice, combi_A, combi_B, dp)
        # print(dp)
        if prob > answer_prob:
            answer_prob = prob
            answer = combi_A
    answer = [x + 1 for x in answer]
    return answer


# 예시 사용법
# dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
# result = solution(dice)
# print(result)

"""
주사위 개수 : n개 -> len(dice)
A가 n/2개 들고갈 때 이길 확률 최대화하기
"""

# 이길 확률 계산
print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))
print(solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]))
# solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4]])
# solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])
"""
18/26
"""
