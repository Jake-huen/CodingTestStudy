n,k = map(int,input().split())
d = [0]*(k+1)
d[0]=1 # 코인1개로
coins=[] # 1 2 5
for i in range(n):
    coins.append(int(input()))
for coin in coins:
    for i in range(coin,k+1):
        d[i]+=d[i-coin]
print(d[k])
