n, m = map(int, input().split())  # 사람 수 , 파티 수

a = list(map(int, input().split()))  # 진실을 아는 사람의 수, 번호
know_people = []
if len(a) > 1:
    know_people = a[1:]

answer = 0
parties = []
for _ in range(m):
    b = list(map(int, input().split()))  # 오는 사람의 수, 번호들
    parties.append(b[1:])
# print("Parties : ", parties)
# print("know_people", know_people)
for _ in range(m):
    for party in parties:
        intersection = [x for x in party if x in know_people]
        if intersection:
            for p in party:
                know_people.append(p)
know_people = list(set(know_people))
# print("kp", know_people)

for party in parties:
    intersection = [x for x in party if x in know_people]
    if intersection:
        continue
    answer += 1
print(answer)
