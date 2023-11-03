n = int(input())
crane = list(map(int, input().split()))
m = int(input())
boxWeight = list(map(int, input().split()))

crane.sort(reverse=True)
boxWeight.sort(reverse=True)

if boxWeight[0] > crane[0]:
    print(-1)
    exit(0)

answer = 0
while boxWeight:
    if not boxWeight:
        break
    for c in crane:
        for box in boxWeight:
            if c >= box:
                boxWeight.remove(box)
                break
    answer += 1

print(answer)
