from itertools import combinations_with_replacement
from collections import deque


def solution(k, n, reqs):
    left_c = n - k  # 일단 타입마다 한명씩 배치해주기
    temp = [i for i in range(k)]
    q = deque()
    answer = 1e9
    for case in combinations_with_replacement(temp, left_c):
        total_time = 0
        left_consultants = [1 for i in range(k)]
        end_time_dict = {i: [] for i in range(k)}  # 끝나는 시간 모두 적어놓기
        for req in reqs:
            q.append(req)
        for tp in case:
            left_consultants[tp] += 1
        while q:
            req = q.popleft()
            start, time, tp = req[0], req[1], req[2]
            end_time_list = end_time_dict[tp - 1].copy()

            for end_time in end_time_dict[tp - 1]:
                if start >= end_time:
                    left_consultants[tp - 1] += 1
                    end_time_list.remove(end_time)

            if left_consultants[tp - 1] > 0:
                left_consultants[tp - 1] -= 1
                end_time_list.append(start + time)
            else:
                total_time += (end_time_list[0] - start)
                end_time = end_time_list.pop(0)
                end_time_list.append(end_time + time)
            end_time_dict[tp - 1] = sorted(end_time_list)

        if answer > total_time:
            answer = total_time
    return answer



print(solution(3, 5,
               [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1],
                [70, 100, 2]]))
