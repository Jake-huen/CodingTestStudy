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
new_graph=defaultdict(list)

for i in range(n):
    if parent[i]!=-1 and parent[i] not in erased and i not in erased:
        new_graph[parent[i]].append(i)

cnt=0
for i in range(n):
    if len(new_graph[i])==0 and (parent[i]==-1 or len(new_graph[parent[i]])!=0) and i not in erased:
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