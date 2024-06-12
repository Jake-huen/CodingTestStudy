# v의 친구 관계 중 루트를 찾기 위한 함수
def find(v):
    if friends[v] < 0:  # 친구가 없는 경우
        return v
    friends[v] = find(friends[v])
    return friends[v]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    friends[b] = a


# 두 번째 조건인 '내 원수의 원수도 내 친구이다'를 위해
# 원수의 원수와 친구 관계를 맺어주기 위한 함수
def findFriends(v):
    for enemy in enemies[v]:  # enemy: 내 원 수
        for friend in enemies[enemy]:  # friend: 내 원수의 원수
            union(v, friend)  # 나와 friend를 union 해준다.


n = int(input())  # 학생의 수
m = int(input())  # 인간관계 개수

friends = [-1 for _ in range(n + 1)]  # 친구 관계 배열
enemies = [[] for _ in range(n + 1)]  # 원수 관계 배열

for _ in range(m):
    a, b, c = map(str, input().split())
    b, c = int(b), int(c)

    if a == 'F':
        union(b, c)  # 친구 관계인 경우 두 학생 유니온
    else:  # 원수 관계인 경우 원수 관계 배열에 추가
        enemies[b].append(c)
        enemies[c].append(b)

# 모든 학생에 대하여 원수의 원수인 학생과 친구를 맺어준다
for i in range(1, n + 1):
    findFriends(i)

# friend들 중 root를 모두 찾음 그 중 0번은 포함 안되니까 뺴기
print(friends.count(-1) - 1)

"""
내 친구의 친구는 내 친구
내 원수의 원수는 내 친구

두 학생이 친구이면 같은 팀에 속해있음.
최대 얼마나 많은 팀이 만들어질 수 있는지 알아내는 프로그램.

친구들만 같은 팀인것은 아님. 친구가 아니라도 같은 팀이 될 수 있다. 
"""
