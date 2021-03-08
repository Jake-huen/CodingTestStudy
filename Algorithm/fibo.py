#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

#탑다운 방식
d = [0]*100
#
# def fibo(x):
#     if x==1 or x==2:
#         retun 1
#     if d[x]!=0:
#         return d[x]
#     d[x]=fibo(x-1)+fibo(x-2)
#     return d[x]

#보텀업 방식
d = [0]*100
d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]  