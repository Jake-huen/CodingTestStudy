t=int(input())
for i in range(t):
    sent = list(input().split())
    for j in range(len(sent)):
        word = list(sent[j])
        ll = len(word)
        for k in range(ll//2):
            word[k],word[ll-1-k]=word[ll-1-k],word[k]
        for k in range(ll):
            print(word[k],end="")
        print(end=" ")
