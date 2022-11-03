n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))
ans=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]=='#':
            temp=0
            while -1<i-temp and i+temp<n and -1<j-temp and j+temp<m and graph[i-temp][j]==graph[i+temp][j]==graph[i][j-temp]==graph[i][j+temp]=='#':
                temp+=1
            while temp:
                ans.append([temp,i,j])
                temp-=1
def check(a,b):
    visited=[[0]*m for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(a[0]):
        for j in range(4):
            visited[a[1]+dx[j]*i][a[2]+dy[j]*i]=1
    for i in range(b[0]):
        for j in range(4):
            if visited[b[1]+dx[j]*i][b[2]+dy[j]*i]==1:
                return False
    return True
answer=0
# print(ans)
for i in range(len(ans)-1):
    for j in range(i+1,len(ans)):
        temp = (1+(ans[i][0]-1)*4)*(1+(ans[j][0]-1)*4)
        if temp>answer and check(ans[i],ans[j]):
            answer=temp
print(answer)

