def palindrom(n):
    n=str(n)
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True
n=int(input())
for i in range(n+1,10**50):
    if palindrom(i)==True:
        print(i)
        break