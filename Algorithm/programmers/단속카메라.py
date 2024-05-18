def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], x[1]))

    start = routes[0][0]
    end = routes[0][1]
    stack = [[start, end]]
    print(routes)
    for i in range(1, len(routes)):
        cur_in, cur_out = routes[i]  # 현재 확인해야되는 차량의 x,y
        print(cur_in, cur_out)
        print()
        flag = False
        for j in range(len(stack)):
            x, y = stack[j]  # x는 cur_x보다 크거나 같음
            # print(x,y)
            if x <= cur_out:  # 겹치는 경우
                print(stack[j])
                stack.pop(j)
                print(max(x, cur_in), min(y, cur_out))
                print()
                print()
                stack.append([max(x, cur_in), min(y, cur_out)])
                flag = True
                break
        if not flag:  # 겹치는게 하나도 없었을 경우
            stack.append([cur_in, cur_out])
    print(stack)

    return answer


solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
