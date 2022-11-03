n=int(input())
zero=[0]*n
one=[0]*n
if n>1:
    zero[1]=1
    one[0]=1
    for i in range(2,n):
        one[i] = one[i-1]+one[i-2]
        zero[i] = zero[i-1]+zero[i-2]
    print(one[n-1]+zero[n-1])
elif n==1:
    print(1)