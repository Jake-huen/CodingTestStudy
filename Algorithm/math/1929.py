#에라토스테네스의 체
"""n=100
a=[]

for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a.append(i)"""
import sys
sys.stdin.readline
m,n = map(int,input().split())
flag=[True]*(n+1)
flag[1]=False
temp = int(n**0.5)
for i in range(2,temp+1):
    if flag[i]==True:
        for j in range(i+i,n+1,i):
            flag[j]=False
for i in range(m,n+1):
    if flag[i]==True:
        print(i)