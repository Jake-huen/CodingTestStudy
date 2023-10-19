# 톱니바퀴 N극은 0, S극은 1
one = list(input())
two = list(input())
three = list(input())
four = list(input())
k = int(input())  # 회전시키는 방법


def turn_left(line):  # 시계 반대방향으로 회전
    return line[1:0]


def turn_right(line):  # 시계 방향으로 회전
    return line[-1:-2]



for _ in range(k):
    num, dir = map(int, input().split())  # 회전시키는 번호, 정수 방향
    # 체크해야하는건 오 왼오 왼오 왼
    print(turn_left(one))
