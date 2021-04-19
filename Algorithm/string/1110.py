n=int(input())
cnt=0
n_n=n
while True:
    first=n_n//10
    second=n_n%10
    n_n=second*10+(first+second)%10
    cnt+=1
    if n_n==n:
        break
    else:
        continue
print(cnt)