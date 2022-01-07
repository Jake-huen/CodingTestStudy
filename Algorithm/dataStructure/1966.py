testcase = int(input())
for _ in range(testcase):
    n,m= map(int,input().split()) #문서의 개수, 궁금한 문서
    s=list(map(int,input().split()))
    count=0
    temp = [0 for _ in range(n)]
    temp[m]=1
    while True:
        if s[0]==max(s):
           count+=1
           if temp[0]==1:
               print(count)
               break
           else:
               del s[0]
               del temp[0]
        else:
            s.append(s[0])
            del s[0]
            temp.append(temp[0])
            del temp[0]



