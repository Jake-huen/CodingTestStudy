#숫자카드 2
import sys
sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
m = int(input())
checks = list(map(int,input().split()))
count={}
for i in data:
    try:count[i]+=1
    except:count[i]=1
for check in checks:
    try:
        print(count[check],end=" ")
    except:
        print(0,end=" ")
#키 값으로 value를 뽑아오는게 더 효율적이다.
