# 항상 X가 선공
# 0:빈칸 1:X 2:O
import sys
input = sys.stdin.readline
graph=[]
for i in range(3):
    graph.append(list(map(int,input().split())))

def game_end(check): #경기 결과 확인
    for i in range(3):
        if graph[i][0]==check and graph[i][1]==check and graph[i][2]==check:
            return True
    for i in range(3):
        if graph[0][i]==check and graph[1][i]==check and graph[2][i]==check:
            return True
    if graph[0][0]==check and graph[1][1]==check and graph[2][2]==check:
        return True
    if graph[0][2]==check and graph[1][1]==check and graph[2][0]==check:
        return True
    return False
def game(turn): # turn=1(2)-> O차례 # turn=0(1) -> X차례
    # -1:LOSE 0:DRAW 1:WIN
    # 놓기 전에 상대가 이긴 경우 turn 1 turn 2
    if game_end(3-turn):
        return -1
    answer=2
    for i in range(3):
        for j in range(3):
            if graph[i][j]==0:
                graph[i][j]=turn
                answer=min(answer,game(3-turn)) # 상대가 이기는지 확인 -> 최선의 수는 여기서 -1이 나오는 경우
                graph[i][j]=0
    if answer==2 or answer==0: # 아무것도 바뀐게 없거나 0
        return 0;
    return -answer

turn=0
for i in range(3):
    for j in range(3):
        if graph[i][j]!=0:
            turn+=1
if turn%2==0:
    answer = game(1) # X 차례 1번 놓기
else:
    answer = game(2) # O 차례 2번 놓기
if answer==1:
    print("W")
elif answer==0:
    print("D")
else:
    print("L")



