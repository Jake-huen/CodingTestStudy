from itertools import permutations

"""
직사각형 모양, 높이는 다르지만 폭은 동일
앞에서 봤을 때 보이는 부분이 s이상만 판매가능

판매가능 그림들의 가격의 합이 최대가 되도록
"""
n, s = map(int, input().split())  # 그림 개수, 판매가능 그림 길이
picture_info = {}
for i in range(n):
    h, c = map(int, input().split())  # 높이, 가격
    picture_info[i] = [h, c]
"""
그림 세우기 -> 전탐색?
"""
cases = list(permutations([i for i in range(n)], n))


def get_price(visible_part):
    result = 0
    for picture_length, price in visible_part:
        if picture_length > s:
            result += price
    return result


answer = 0
for case in cases:
    #  case : 배치 순서
    visible_part = [[picture_info[case[0]][0], picture_info[case[0]][1]]]  # 첫번째 그림 높이
    temp = picture_info[case[0]][0]  # 현재 제일 높은 그림 높이
    for i in range(1, n):
        result = picture_info[case[i]][0] - temp
        visible_part.append([result, picture_info[case[i]][1]])
        temp = max(picture_info[case[i]][0], temp)  # 현재 제일 높은 그림 높이
    # print(case)
    # print(visible_part)
    answer = max(answer, get_price(visible_part))
print(answer)
"""
30만!
"""