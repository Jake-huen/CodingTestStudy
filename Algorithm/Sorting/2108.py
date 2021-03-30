from collections import Counter
import sys
n = int(sys.stdin.readline())

datas=[]
for _ in range(n):
    datas.append(int(sys.stdin.readline()))

def first(datas):
    return round(sum(datas)/len(datas))

def second(datas):
    datas.sort()
    mid = (len(datas))//2
    return datas[mid]

def third(datas):
    mode_dict = Counter(datas)
    modes = mode_dict.most_common()

    if len(datas) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

def fourth(datas):
    return max(datas)-min(datas)

print(first(datas))
print(second(datas))
print(third(datas))
print(fourth(datas))