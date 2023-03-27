# p : 1,4,5,3,2
# D : 4,3,1,2,5
n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))
temp = [0 for _ in range(n + 1)]
for _ in range(k):
    for i in range(1, n + 1):
        temp[d[i]] = s[i]
    s = temp
    temp = [0 for _ in range(n + 1)]
for i in range(1,n+1):
    print(s[i],end=' ')
