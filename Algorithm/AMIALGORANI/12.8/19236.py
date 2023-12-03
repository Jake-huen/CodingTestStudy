fish = {i: [] for i in range(1, 15)}
for row in range(4):
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), 2):
        fish_number = temp[i]
        fish_dir = temp[i + 1]
        fish_place = [row, i // 2]
        fish[fish_number] = [fish_dir, fish_place]
shark = [0, 0]  # 처음 위치

# dir 1위 2왼위 3왼 4왼아 5아 6오아 7오 8오위
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
answer = []


def shark_init():
    for fish_number in range(1, 16):
        f_x, f_y = fish[fish_number][1]
        if f_x == shark[0] and f_y == shark[1]:
            answer.append(fish_number)
            del fish[fish_number]


def fish_move():
    for fish_number in range(1, 16):
        if fish_number in fish:  # 물고기가 존재하는 경우
            x, y = fish[fish_number][1]  # 시작할때 물고기의 위치
            dir = fish[fish_number][0]  # 시작할때 물고기의 방향
            dir2 = dir
            while True:
                nx = x + dx[dir2]
                ny = y + dy[dir2]
                is_moved = False  # 움직임 여부(움직임 없으면 방향 바꿔주기 위함)
                if 0 <= nx < 4 and 0 <= ny < 4 and nx != shark[0] and ny != shark[1]:
                    flag = False  # 교환 여부
                    for fish_number2 in range(1, 16):
                        if fish_number2 in fish:
                            f_x, f_y = fish[fish_number2][1] # 교환할 물고기 위치
                            if f_x == nx and f_y == ny and fish_number != fish_number2:
                                fish[fish_number][0] = dir2
                                fish[fish_number][1] = [f_x, f_y]
                                fish[fish_number2][1] = [x, y]
                                flag = True
                                is_moved = True
                                print("[교환]물고기 번호 : ", fish_number, fish_number2)
                    if not flag:
                        fish[fish_number][0] = dir2
                        fish[fish_number][1] = [nx, ny]
                        is_moved = True
                        print("[빈칸]물고기 번호 : ", fish_number)
                if is_moved:
                    break
                if not is_moved:
                    print("[방향 전환]물고기 번호 : ", fish_number)
                    dir2 = (dir2 + 1)
                    if dir2 == 9:
                        dir2 = 1
                    if dir2 == dir:
                        print("[움직일 곳 없음]물고기 번호 : ", fish_number)
                        break  # 움직일 곳이 없음


shark_init()
fish_move()
print(fish)

"""
한 사이클
1. 물고기 이동
- 번호가 작은 물고기부터 이동
    - 이동가능 : 빈 칸, 다른 물고기 있는 칸
    - 이동불가능 : 상어있는 칸, 공간 경계 넘는 칸
    - 이동가능한 칸이 있을 때까지 방향 45도 반시계 회전시킴
    - 이동가능한 칸 없으면 이동하지 않음
2. 상어 이동
- 방향이 있는 칸으로 이동
    - 물고기 있는 칸으로 이동 -> 그 칸의 물고기 먹고 방향 가짐
    - 물고기 없는 칸으로 이동 불가능
    - 이동가능한 칸이 없을 때 끝남
- 처음에는 상어(0,0)에 있는 물고기를 먹음
"""
