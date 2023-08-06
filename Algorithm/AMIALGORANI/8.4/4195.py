t = int(input())
graph = []
for _ in range(t):
    f = int(input()) # 친구 관계의 수
    for _ in range(f):
        friends = list(input().split(' '))
        print(friends)

