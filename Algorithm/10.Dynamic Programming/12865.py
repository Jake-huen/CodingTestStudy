#냅색 알고리즘 knapsack algorithm
"""
0-1배낭문제(Knapsack Problem)
x축엔 가방 1~K까지의 무게, y축은 물건 N개 개수 만큼의 배열
행을 차례대로 돌며 알고리즘 실행

knapsack[i][j]=
max(현재 물건 가치+knapsack[이전물건][현재 가방 무게-현재 물건 무게],
knapsack[이전물건][현재 가방 무게])
"""
n,k = map(int,input().split())
things=[[0,0]]
knapsack=[[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
    things.append(list(map(int,input().split())))
# print(things)
# print(knapsack)
for i in range(1,n+1):
    for j in range(1,k+1):
        value=things[i][1]
        weight=things[i][0]
        if j<weight:
            knapsack[i][j]=knapsack[i-1][j]
        else:
            knapsack[i][j]=max(value+knapsack[i-1][j-weight],knapsack[i-1][j])
print(knapsack[n][k])