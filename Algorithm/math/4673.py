def d(n):
    x=0
    a=list(str(n))
    for i in a:
        x=x+int(i)
    return n+x
s_set=set()
for i in range(1,10000):
    s_set.add(d(i))
ans=set(range(1,10000))-s_set
for num in sorted(ans):
    print(num)