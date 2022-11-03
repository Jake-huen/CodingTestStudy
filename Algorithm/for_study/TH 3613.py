temp=list(input())
def cppjava(s):
    underbar=0
    upper=0
    if s[0].isupper():
        return 'ERROR'
    if s[0]=='_':
        return 'ERROR'
    if s[-1]=='_':
        return 'ERROR'
    for i in range(len(s)):
        if s[i].isupper():
            upper+=1
        elif s[i]=='_':
            underbar+=1
    if upper==0 and underbar>=0:
        return 'C'
    else:
        return 'JAVA'
def javatocpp(s):
    temp=''
    for ch in s:
        check = ord(ch)
        if ord('A')<=check<=ord('Z'):
            temp+='_'
            temp+=ch.lower()
        else:
            temp+=ch
    return temp
def cpptojava(s):
    temp=''
    upper=False
    for ch in s:
        if ch=='_':
            upper=True
        else:
            if upper:
                temp+=ch.upper()
                upper=False
            else:
                temp+=ch
    return temp
if len(temp)==0:
    print('Error')
elif cppjava(temp)=='C':
    print(cpptojava(temp))
elif cppjava(temp)=='JAVA':
    print(javatocpp(temp))
else:
    print('Error!')


