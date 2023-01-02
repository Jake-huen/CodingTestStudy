a,b = map(int,input().split())
n,m = map(int,input().split())
robots=[]
for i in range(n):
    x, y, direction = list(input().split()) # 로봇의 위치, 방향
    robots.append(list((int(x),int(y),direction))) # 1 1 E
# print(robots)
def do_order(x,y,dir,order): #x,y:현재 위치 order:명령
    # order = (1,F,7)
    if order == 'F':
        if dir=='E':
            x+=1
        elif dir=='W':
            x-=1
        elif dir=='N':
            y+=1
        elif dir=='S':
            y-=1
        return x,y,dir
    elif order == 'L':
        if dir=='E':
            dir='N'
        elif dir=='S':
            dir='E'
        elif dir=='W':
            dir='S'
        elif dir=='N':
            dir='W'
        return x,y,dir
    elif order=='R':
        if dir == 'E':
            dir= 'S'
        elif dir == 'S':
            dir ='W'
        elif dir == 'W':
            dir ='N'
        elif dir == 'N':
            dir ='E'
        return x,y,dir

for i in range(m):
    robot,order,count = input().split() # 1 F 7
    robot = int(robot)-1
    count = int(count)
    x,y,dir = robots[robot][0],robots[robot][1],robots[robot][2] # 움직여야 되는 로봇의 x,y좌표와 방향
    for j in range(int(count)):
        x,y,dir = do_order(x,y,dir,order)
        robots[robot][0]=x
        robots[robot][1]=y
        robots[robot][2]=dir
        for k in range(len(robots)):
            if x == robots[k][0] and y == robots[k][1]:
                if k!=robot:
                    print(f'Robot {robot+1} crashes into robot {k+1}')
                    exit(0)
        if x<0 or x>n or y>n or y<0:
            print(f"Robot {robot+1} crashes into the wall")
            exit(0)
        print(robots)
print("OK")




"""
5 4
2 2
1 1 E
5 4 W
1 F 7
2 F 7
Robot 1 crashes into the wall

5 4
2 4
1 1 E
5 4 W
1 F 3
2 F 1
1 L 1
1 F 3
Robot 1 crashes into robot 2

5 4
2
2 2
1 1 E
5 4 W
1 L 96
1 F 2
OK

5 4
2 3
1 1 E
5 4 W
1 F 4
1 L 1
1 F 20
Robot 1 crashes into robot 2
"""