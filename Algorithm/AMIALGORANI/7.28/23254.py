import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
heap = []
for i in range(m):
    heapq.heappush(heap, [-b[i], a[i]])
time = 0
answer = 0
while 24 * n > time and heap:
    x, y = heapq.heappop(heap)  # 공부효율, 현재 성적
    x = -x
    if (100 - y) // x < 24 * n - time:  # 현재 최대값까지 갈 수 있는 시간이 되는지 여부 확인
        temp = y + (x * ((100 - y) // x))
        if temp == 100:
            answer += 100
        else:
            heapq.heappush(heap, [-(100 - temp), temp])
        time += (100 - y) // x
    else:
        answer += y + (24 * n - time) * x
        time += (24 * n - time)
for a, b in heap:
    answer += b
print(answer)
