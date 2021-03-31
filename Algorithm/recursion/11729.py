n=int(input())
def move_check(start,end):
    print(start,end)
def hanoi(move,start,end):
    if move==1:
        return move_check(start,end)
    other=6-start-end
    hanoi(move-1,start,other)
    move_check(start,end)
    hanoi(move-1,other,end)
sum=1
for i in range(n-1):
    sum=sum*2+1
print(sum)
hanoi(n,1,3)