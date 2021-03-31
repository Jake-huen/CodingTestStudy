n= int(input())
def star(n):
    global Map
    if n==3:
        Map[0][:3]=Map[2][:3]=[1]*3
        Map[1][:3]=[1,0,1]
        return
    a=n//3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)]=Map[k][:a]


def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix


star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)
