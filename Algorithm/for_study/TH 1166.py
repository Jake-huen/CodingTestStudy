n,l,w,h = map(int,input().split())
# n : 작은 박스 개수 l,w,h : 가로 세로 높이
s,e = 0, max(l,w,h)
for _ in range(100):
    m = (s+e)/2
    count = (l//m)*(w//m)*(h//m)
    if count>=n:
        s=m
    else:
        e=m
print("%.10f" %e)