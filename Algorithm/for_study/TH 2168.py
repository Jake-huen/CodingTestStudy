x,y = map(int,input().split())
# 가로 x, 세로 y
# 최대공약수
gcd=0
for i in range(min(x,y),0,-1):
    if x%i==0 and y%i==0:
        gcd=i
        break
# (x//gcd y//gcd) * gcd
print(x+y-gcd)
# def gcb(a,b):
#     tmp=a%b
#     while tmp!=0:
#         a=b
#         b=tmp
#         tmp=a%b
#     return abs(b)
#
# print(x+y-gcb(x,y))