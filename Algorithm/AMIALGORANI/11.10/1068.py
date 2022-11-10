from collections import deque,defaultdict
import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int,input().split()))
erase_node = int(input())
graph = defaultdict(list)

for i in range(n):
    if parent[i]!=-1:
        graph[parent[i]].append(i)

q=deque()
q.append(erase_node)
erased = []

while q:
    x = q.pop()
    erased.append(x)
    for i in graph[x]:
        q.append(i)
new_graph=defaultdict(list) #지워버리고 보여줘야지

for i in range(n):
    if parent[i] not in erased and i not in erased: #부모가 안 지워졌거나 나 자신도 안지워졌을때
        new_graph[parent[i]].append(i)

cnt=0
for i in range(n): # 자식이 없고, 부모가 자식 가지고 있을때이고, 내가 지워지지 않았을때..
    if len(new_graph[i])==0 and len(new_graph[parent[i]])!=0 and i not in erased:
        cnt+=1
print(cnt)

'''
2
-1 0
1

9
-1 0 0 5 2 4 4 6 6
4
'''