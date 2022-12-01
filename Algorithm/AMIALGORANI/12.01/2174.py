a,b = map(int,input().split())
n,m = map(int,input().split())
orders=[]
robots=[]
for i in range(n):
    x, y, direction = list(input().split())
    robots.append(list((int(x),int(y),direction)))
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
    robot,order,count = input().split()
    x,y,dir = robots[int(robot)-1][0],robots[int(robot)-1][1],robots[int(robot)-1][2]
    for j in range(int(count)):
        if j==0:
            x_temp,y_temp,dir_temp = do_order(x,y,dir,order)
        else:
            x_temp,y_temp,dir_temp = do_order(x_temp,y_temp,dir_temp,order)
        robots[int(robot)-1][0]=x_temp
        robots[int(robot)-1][1]=y_temp
        robots[int(robot)-1][2]=dir_temp
        for k in range(len(robots)):
            if x_temp == robots[k][0] and y_temp == robots[k][1]:
                if k+1!=int(robot):
                    print(f'Robot {robot} crashes into robot {k+1}')
                    exit(0)
        if x_temp<0 or x_temp>n or y_temp>n or y_temp<0:
            print(f"Robot {robot} crashes into the wall")
            exit(0)
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