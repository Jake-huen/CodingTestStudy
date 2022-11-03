from itertools import combinations
n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
# 일단 치킨집의 개수 알고 -> 여기서 m개를 골라서 브루트 포스?
chickens=[]
houses = []
answer=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chickens.append((i,j))
        elif graph[i][j]==1:
            houses.append((i,j))
selected_chickens = list(combinations(chickens,m)) # 조합으로 m개만큼 고른 치킨집들
for selected_chicken in selected_chickens: #조합 중 하나씩 해보기
    distance = []
    for house in houses: #각각의 집에서
        chicken_distance = (n - 1) + (n - 1)  # 제일 max로 잡아둠
        for chicken in selected_chicken: #모든 치킨집중 어디가 젤 가까운지 테스트
            chicken_distance = min(chicken_distance,abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))
        distance.append(chicken_distance)
    temp=0
    for i in range(len(distance)):
        temp+=distance[i]
    answer.append(temp)
print(min(answer))