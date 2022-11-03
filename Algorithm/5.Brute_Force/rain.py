# def trapping_rain(buildings):
#     # 코드를 작성하세요
#     big= buildings[0]
#     r_max = max(buildings)
#     result = 0
#     for i in range(len(buildings)-1):
#         if buildings[i]<=big:
#             result+=big-buildings[i]
#         else:
#             if buildings[i]!=r_max:
#                 big=buildings[i]
#             else:continue
#     return result
#이 해답은 제일 높은 키의 건물이 2개 이상이 되는 경우 사용할 수 없다.

#더 큰 건물들 사이에 끼여있으면 빗물이 담기는 것.
#1. 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이를 구한다
#2. 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이를 구한다
#3. 그 중 더 낮은 건물의 높이를 구한다
#4. 그 높이에서 현재 인덱스에 있는 건물의 높이를 뺀다.

def trapping_rain(buildings):
    total=0
    for i in range(1,len(buildings)-1):
        max_left=max(buildings[:i])
        max_right=max(buildings[i:])

        upper_bound = min(max_left,max_right)

        total += max(0,upper_bound-buildings[i])
    return total
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))