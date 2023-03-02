s = list(input())
t = list(input())


def way(temp):
    if temp[-1] == 'A':
        return temp[0:-1]
    elif temp[-1] == 'B':
        temp = temp[0:-1]
        return temp[::-1]


ans = t
while True:
    if ans == s:
        print(1)
        break
    else:
        if len(ans)>len(s):
            ans = way(ans)
        else:
            print(0)
            break
