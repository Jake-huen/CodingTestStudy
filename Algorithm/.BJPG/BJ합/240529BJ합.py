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
sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
assignments = {}

non_zero_candidates = [item[0] for item in sorted_dict if not item[1][0]]

current_number = 9


for candidate in non_zero_candidates:
    assignments[candidate] = current_number
    current_number -= 1

for char, values in sorted_dict:
    if char not in assignments:
        assignments[char] = current_number
        current_number -= 1
print(assignments)
total = 0
for input in inputs:
    m = 1
    for i in range(len(input) - 1, -1, -1):
        total += assignments[input[i]] * m
        m *= 10
print(total)
