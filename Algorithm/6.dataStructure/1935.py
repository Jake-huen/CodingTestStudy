n = int(input())
sen = input()
s=[]
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
for a in sen:
    if a.isupper():
        s.append(nums[ord(a)-ord('A')])
    elif a=='+':
        one = s.pop()
        two = s.pop()
        s.append(two+one)
    elif a=='-':
        one = s.pop()
        two = s.pop()
        s.append(two-one)
    elif a=='*':
        one = s.pop()
        two = s.pop()
        s.append(two*one)
    elif a=='/':
        one = s.pop()
        two = s.pop()
        s.append(two/one)
print("{:.2f}".format(s[0]))

