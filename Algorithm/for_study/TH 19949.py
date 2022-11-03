exam_ans = list(map(int,input().split()))
# def check(fake,real):
#     ans=0
#     for i in range(10):
#         if fake[i]==real[i]:
#             ans+=1
#     if ans>=5:
#         return True
#     else:
#         return False

def dfs(depth):
    global cnt
    if depth==10:
        temp=0
        for i in range(10):
            if li[i]==exam_ans[i]:
                temp+=1
        if temp>=5:
            cnt+=1
    for i in range(1,6):
        if depth>=2 and li[depth-2]==li[depth-1]==i:
            continue
        li.append(i)
        dfs(depth+1)
        li.pop()
li=[]
cnt=0
dfs(0)
print(cnt)

