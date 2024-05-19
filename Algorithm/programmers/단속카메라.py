def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1]))
    # print(routes)
    key = -300001
    for route in routes:
        if route[0] > key:
            answer += 1
            key = route[1]
    # print(answer)
    return answer


solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
