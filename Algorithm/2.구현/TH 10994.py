n = int(input())
for i in range(1,n):
    temp = (n-i)*4+1
    print('* '*(i-1)+'*'*temp+' *'*(i-1))
    print('* '*i+' '*(temp-4)+' *'*i)
print('* '*(n*2-1))
for i in range(n-1,0,-1):
    temp = (n-i)*4+1
    print('* '*i+' '*(temp-4)+' *'*i)
    print('* '*(i-1)+'*'*temp+' *'*(i-1))
