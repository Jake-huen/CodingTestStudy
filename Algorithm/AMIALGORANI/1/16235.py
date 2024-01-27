"""
가장 처음에 양분은 모든 칸에 5
m개의 나무를 구매해 땅에 심음 -> 같은 칸에 여러 개의 나무가 심어져 있을 수도 있다.
봄 : 자신의 나이만큼 양분 -> 나이 1증가 /
    칸에 있는 양분만 먹을 수 있음 -> 칸에 여러 개의 나무가 있다면 나이 어린 나무부터 양분 먹음
    땅에 양분 부족 -> 죽음
여름 : 봄에 죽은 나무가 양분으로 변함 / 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
가을 : 나무 번식 / 번식하는 나무는 나이가 5의 배수여야 함.
겨울 : 땅에 양분 추가 -> 각 칸에는 A[r][c]만큼 추가됨.
K년 지난 후에 상도의 땅에 살아있는 나무의 개수 구하기
"""

n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
tree = [[[5] for _ in range(n + 1)] for _ in range(n + 1)]
print(tree)

# def spring():
#
#
# def summer():
#
#
# def autumn():
#
#
# def winter():


for _ in range(m):
    x, y, z = map(int, input().split())  # 나무 위치 , 나무 나이
