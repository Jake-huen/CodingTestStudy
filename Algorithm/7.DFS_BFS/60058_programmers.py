def solution(p):
    answer = ''
    if p == '':
        return p
    if check(p):
        return p
    u=sep(p)[0]
    v=sep(p)[1]
    if check(u):
        return u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u=u[1:-1]
        for i in reverse(u):
            answer+=i
        # u = u[1:-1]
        # return ["("] + recursive(v) + [")"] + reverse(u)
        return answer


def check(p):
    x = y = 0
    for i in range(len(p)):
        if p[i] == '(':
            x += 1
        elif p[i] == ')':
            y += 1
        if x < y:
            return False
    return True


def sep(p):
    x = y = 0
    num = 0
    u = ''
    v = ''
    while True:
        if p[num] == '(':
            x += 1
        elif p[num] == ')':
            y += 1
        num += 1
        if x == y:
            for i in range(num):
                u += p[i]
            for j in range(num, len(p)):
                v += p[j]
            break
    return u,v
def reverse(strings):
    r = {"(":")", ")": "("}
    return [r[s] for s in strings]
print(solution("()))((()"))
# print(reverse(')('))
