n = int(input())
k=0
def move_check(start,end):
    print(start,end)
def hanoi(move,start,end):
    if move==1:
        return move_check(start,end)
    other=6-start-end
    hanoi(move-1,start,other)
    move_check(move,start,end)
    hanoi(move-1,other,end)

hanoi(n,1,3)