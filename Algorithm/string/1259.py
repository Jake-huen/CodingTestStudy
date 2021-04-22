def palindrom(n):
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True

while True:
    n=input()
    if n=='0':
        break
    else:
        if palindrom(n)==True:
            print('yes')
        else:
            print('no')
