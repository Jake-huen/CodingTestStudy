n,m = map(int,input().split())
s=set()
for i in range(n):
    s.add(input())
# print(s)
count=0
for i in range(m):
    temp = input()
    if temp in s:
        count+=1
print(count)