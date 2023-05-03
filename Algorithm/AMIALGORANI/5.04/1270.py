n = int(input())  # 땅의 개수
answers = []
for _ in range(n):
    temp = list(map(int, input().split()))  # 땅의 병사 수, 각각 병사의 군대 번호
    soldier_map = {}
    check = temp[0] // 2 + 1
    soldiers = temp[1:]
    answer = 0
    for soldier in soldiers:
        if soldier in soldier_map.keys():
            soldier_map[soldier] += 1
            if soldier_map[soldier] >= check:
                answer = soldier
        else:
            soldier_map[soldier] = 1
    if answer == 0:
        answers.append("SYJKGW")
    else:
        answers.append(answer)
for answer in answers:
    print(answer)
