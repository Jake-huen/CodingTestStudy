import sys

input = sys.stdin.readline
n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()
start = 1
end = houses[-1]
answer = 0
while start <= end:
    houseNumber = 1  # 시작집은 일단 추가시키기
    # distance = (end-start)//2
    distance = (start + end) // 2
    current = houses[0]
    for i in range(1, len(houses)):
        if houses[i] >= current + distance:
            current = houses[i]
            houseNumber += 1
    if houseNumber >= c:  # distance를 너무 짧게 잡았으므로 늘리기
        start = distance + 1
        answer = distance
    else:  # distance를 너무 길게 해서 원하는 공유기 개수가 안나오므로 distance 줄이기
        end = distance - 1
print(answer)
