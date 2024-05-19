# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: (x[0], x[1]))
#
#     start = routes[0][0]
#     end = routes[0][1]
#     stack = [[start, end]]
#     print(routes)
#     for i in range(1, len(routes)):
#         cur_in, cur_out = routes[i]  # 현재 확인해야되는 차량의 x,y
#         print(cur_in, cur_out)
#         print()
#         flag = False
#         for j in range(len(stack)):
#             x, y = stack[j]  # x는 cur_x보다 크거나 같음
#             # print(x,y)
#             if x <= cur_out:  # 겹치는 경우
#                 print(stack[j])
#                 stack.pop(j)
#                 print(max(x, cur_in), min(y, cur_out))
#                 print()
#                 print()
#                 stack.append([max(x, cur_in), min(y, cur_out)])
#                 flag = True
#                 break
#         if not flag:  # 겹치는게 하나도 없었을 경우
#             stack.append([cur_in, cur_out])
#     print(stack)
#
#     return answer
#
#
def solution(routes):
    # 진출지점에 대해서 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    # 기준은 제한사항 참조
    key = -30001
    # 필요한 카메라 수
    cnt = 0

    for route in routes:
        # 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
            # 단속이 안되기에 카메라 하나 더 필요
            cnt += 1
            # 새로운 기준은 해당 경로의 진출지점(맨끝)
            key = route[1]

    return cnt
solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
