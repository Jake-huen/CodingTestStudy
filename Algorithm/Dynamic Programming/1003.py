# 피보나치 함수

T = int(input())

zero = [0]*42
one = [0]*42
zero[0]=1
one[1]=1
for _ in range(T):
    n = int(input())
    for i in range(2,n+1):
        zero[i]=zero[i-1]+zero[i-2]
        one[i]=one[i-1]+one[i-2]
    print(zero[n],one[n])

