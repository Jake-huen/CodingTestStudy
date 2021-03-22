n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
for i in range(n):
    print(data[i])