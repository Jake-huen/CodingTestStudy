a = list(input())
b = list(input())

def way1(temp):
    return temp[1:]
def way2(temp):
    cnt = 0
    cp = '0'
    for l in temp:
        if l == '1':
            cnt += 1
    if cnt % 2 == 1:
        cp = '1'
    return temp + cp

