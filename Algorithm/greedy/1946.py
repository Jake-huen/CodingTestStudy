import sys
t=int(input())
answers=[]
for _ in range(t):
    score=[]
    ans=[]
    n = int(input())
    for i in range(n):
        x,y=map(int,sys.stdin.readline().split())
        score.append((x,y))
    score=sorted(score,key=lambda x:x[0])
    ans.append(score[0])
    for i in range(1,n):
        if score[i][1]<ans[-1][1]:
            ans.append(score[i])
    answers.append(len(ans))
for answer in answers:
    print(answer)