from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque('' for _ in range(cacheSize))
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            flag = True
            for i in range(len(cache)):
                if cache[i] == '':
                    cache[i] = city
                    answer += 5
                    flag = False
                    break
                else:
                    continue
            if flag:
                answer += 5
                if len(cache) > 0:
                    cache.popleft()
                    cache.append(city)
    return answer