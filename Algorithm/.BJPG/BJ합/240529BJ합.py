n = int(input())
dict = {}
inputs = []
for _ in range(n):
    temp = list(input())
    inputs.append(temp)
    m = 1
    for i in range(len(temp) - 1, -1, -1):
        if temp[i] in dict.keys():
            if i == 0:  # 첫번째 자리인 경우
                dict[temp[i]][0] = False  # 0이 올 수 없음
                dict[temp[i]][1] += m
            else:
                dict[temp[i]][1] += m
        else:
            if i == 0:
                dict[temp[i]] = [False, m]
            else:
                dict[temp[i]] = [True, m]
        m *= 10
sorted_dict = sorted(dict.items(), key=lambda x: x[1][1], reverse=True)

total = 0
count = 9
if len(sorted_dict) > 9:
    for i in range(9, -1, -1):
        if sorted_dict[i][1][0]:
            temp = sorted_dict[i]
            sorted_dict.remove(temp)
            sorted_dict.append(temp)
            break
# print(sorted_dict)
for i in range(len(sorted_dict)):
    total += sorted_dict[i][1][1] * (9 - i)
print(total)
