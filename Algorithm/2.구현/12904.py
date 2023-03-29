s = list(input())
t = list(input())


def wayone(temp):
    return temp[:-1]


def waytwo(temp):
    temp = temp[:-1]
    return temp[::-1]

while True:
    if t[-1] == 'A':
        t = wayone(t)
    elif t[-1] == 'B':
        t = waytwo(t)
    if s == t:
        print("1")
        break
    else:
        if len(t) == 0:
            print("0")
            break
        else:
            continue
