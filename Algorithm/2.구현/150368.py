from itertools import product

def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    ways = list(product(discounts, repeat=len(emoticons)))
    for way in ways:
        t1 = 0
        t2 = 0
        for user in users:
            sum = 0
            for idx, emoticon in enumerate(emoticons):
                if way[idx] >= user[0]:
                    sum += emoticon * ((100 - way[idx]) / 100)
            # 6300 9000 7200
            if sum >= user[1]:
                t1 += 1
            else:
                t2 += sum
        answer.append([t1, int(t2)])
    answer = sorted(answer, reverse=True, key=lambda x: (x[0], x[1]))
    return answer[0]


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
