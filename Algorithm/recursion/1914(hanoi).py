n = int(input())
k=0
def move_check(start,end):
    print(start,end)
def hanoi(move,start,end):
    if move==1:
        return move_check(start,end)
    other=6-start-end
    hanoi(move-1,start,other)
    move_check(start,end)
    hanoi(move-1,other,end)
sum=0
for i in range(n):
    sum=sum*2+1

if n>20:
    print(sum)
else:
    print(sum)
    hanoi(n,1,3)
