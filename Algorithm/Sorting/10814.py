n = int(input())

data = []
for i in range(n):
    age, name = list(input().split())
    age=int(age)
    data.append((age, name, i))
data = sorted(data, key=lambda x: x[0])

for i in range(n):
    print(str(data[i][0]) + ' ' + data[i][1])


#x[0]와 x[2]의 type이 무엇인지 고민. int인지 string인지에 따라 비교가 다르게 된다.