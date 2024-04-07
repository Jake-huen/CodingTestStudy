n = int(input())
work = [[] for _ in range(1001)]
for _ in range(n):
    d, w = map(int, input().split())  # 과제 마감일까지 남은 일수, 과제 점수
    work[d].append(w)
answer = 0
for i in range(len(work) - 1, 0, -1):
    if len(work[i]) >= 1:
        temp = sorted(work[i])
        #print(temp)
        answer += temp[-1]
        for j in range(len(temp) - 1):
            #print("temp[j], ", temp[j])
            work[i - 1].append(temp[j])
    else:
        continue
print(answer)


"""
과제 날짜가 제일 많이 남은 날짜에서부터 배열 중 점수가 가장 큰 거 하나씩 더하고,
남은 건 날짜-1의 배열에 추가해서 1일까지 계산.
"""