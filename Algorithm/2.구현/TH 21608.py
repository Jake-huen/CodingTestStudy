# 교실 : N X N -> N제곱 학생들이 자리 정함.
# 각 학생이 좋아하는 학생 4명도 모두 조사했음.
# 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리
n = int(input())
c_student = n**2+1
student = [[] for _ in range(c_student)]
arr = [[0]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(c_student-1):
    a,b,c,d,e = list(map(int,input().split()))
    student[a].append(b)
    student[a].append(c)
    student[a].append(d)
    student[a].append(e)
    m_near=0
    m_empty=0
    temp_x=0
    temp_y=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                near = 0
                empty =9999 #어떤 값이든 상관이 없다.
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if nx>=0 and nx<n and ny>=0 and ny<n:
                        if arr[nx][ny] in student[a]:
                            near+=1
                        if arr[nx][ny]==0:
                            empty+=1
                if near>m_near:
                    m_near = near
                    m_empty = empty
                    temp_x=i
                    temp_y=j
                if near==m_near and empty>m_empty:
                    m_empty=empty
                    temp_x=i
                    temp_y=j

    arr[temp_x][temp_y] = a
# print(arr)
answer=0
for i in range(n):
    for j in range(n):
        temp=0
        stud = arr[i][j]
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if arr[nx][ny] in student[stud]:
                    temp+=1
        if temp==0:
            answer+=0
        elif temp==1:
            answer+=1
        elif temp==2:
            answer+=10
        elif temp==3:
            answer+=100
        elif temp==4:
            answer+=1000
print(answer)