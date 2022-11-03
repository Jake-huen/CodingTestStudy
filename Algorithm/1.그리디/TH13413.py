t = int(input())
arr=[]
ans=0
answer=[]
for i in range(t):
    n = int(input())
    first = input()
    second = input()

    for i in range(n):
        if first[i]!=second[i]:
            arr.append(first[i])
    if arr.count('B')>=arr.count('W'):
        ans=arr.count('B')
    else:
        ans = arr.count('W')
    answer.append(ans)
    arr=[]
for a in answer:
    print(a)


