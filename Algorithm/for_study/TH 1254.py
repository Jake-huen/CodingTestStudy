s = input()
def check(temp):
    r = len(temp)//2
    for i in range(r):
        if temp[i]==temp[len(temp)-i-1]:
            continue
        else:
            return False
    return True
ans=0
for i in range(len(s)):
    if check(s[i:]):
        break
    else:
        ans+=1
print(ans+len(s))
