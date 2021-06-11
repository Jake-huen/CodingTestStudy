n = int(input())
score=list(map(int,input().split()))
target = max(score)
answer=0
for i in range(len(score)):
    temp = score[i]/target*100
    answer+=temp
answer=answer/len(score)
print(answer)