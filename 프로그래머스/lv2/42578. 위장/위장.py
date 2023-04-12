def solution(clothes):
    ways = {}
    for cloth in clothes:
        if cloth[1] in ways.keys():
            ways[cloth[1]].append(cloth[0])
        else:
            ways[cloth[1]] = [cloth[0]]
    # print(len(ways.keys()))
    ans = 1
    for key in ways.keys():
        ans = ans * (len(ways[key])+1)
    ans-=1
    return ans