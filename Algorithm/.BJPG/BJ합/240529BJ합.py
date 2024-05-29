n = int(input())
dict = {}
for _ in range(n):
    temp = list(input())
    m = 1
    for i in range(len(temp) - 1, -1, -1):
        if temp[i] in dict.keys():
            if i == 0:  # 첫번째 자리인 경우
                dict[i][0] = False  # 0이 올 수 없음
                dict[i][1] += m
            else:
                dict[i][1] += m
        else:
            if i == 0:
                dict[i] = [False, m]
            else:
                dict[i] = [True, m]
        m *= 10
print(dict)
