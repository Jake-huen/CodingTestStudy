h, w = map(int, input().split())
graph = list(map(int, input().split()))
check = max(graph)
max_index = []
for i in range(len(graph)):
    if graph[i] == check:
        max_index.append(i)
left = []
middle = []
right = []
answer = 0
for i in range(len(graph)):
    if i < max_index[0]:
        left.append(graph[i])
    elif i > max_index[-1]:
        right.append(graph[i])
    else:
        middle.append(graph[i])
if len(left) > 0:
    check = left[0]
    for i in range(1, len(left)):
        if left[i] < check:
            answer += check - left[i]
        elif left[i] > check:
            check = left[i]
# print(answer)
if len(right) > 0:
    check = right[-1]
    for i in range(len(right) - 1, -1, -1):
        if right[i] < check:
            answer += check - right[i]
        elif right[i] > check:
            check = right[i]
# print(answer)
if len(middle) > 0:
    check = max(middle)
    for i in range(len(middle)):
        answer+= check - middle[i]
print(answer)
# for i in range(len(left)):

'''
5 5
5 1 3 1 5
'''
