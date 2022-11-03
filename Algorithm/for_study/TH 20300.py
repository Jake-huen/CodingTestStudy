# 운동기구 2개까지만 선택가능
# N개 사용해보고 싶음
# 근손실 M 안넘도록 하기
n = int(input())
t = list(map(int,input().split()))
t.sort()
if len(t)%2==0: #짝수
    ans=0
    for i in range(len(t)//2):
        ans=max(ans,t[i]+t[len(t)-i-1])
else:
    ans=0
    for i in range(len(t)//2):
        ans=max(ans,t[i]+t[len(t)-i-2])
    ans=max(t[-1],ans)
print(ans)
