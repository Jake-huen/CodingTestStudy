l,r = input().split()
sent = input()
keyboard=[
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
]
def pl(temp):
    for i,key in enumerate(keyboard):
        if temp in key:
            return i,key.index(temp)
    return None
lx,ly = pl(l)
rx,ry = pl(r)
answer=0
for i in range(sent):
    x,y = pl(i)
    if((x==0 or x==1) and y<5) or (x==2 and y<4):
        answer+=abs(lx-x)+abs(ly-y)
        lx = x
        ly = y
        answer+=1
    else:
        answer+=abs(rx-x)+abs(ry-y)
        rx=x
        ry=y
        answer+=1
print(answer)