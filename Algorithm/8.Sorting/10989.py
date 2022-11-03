import sys
input = sys.stdin.readline

n = int(input())
data=[0]*10001
for _ in range(n):
    num = int(input())
    data[num-1]+=1

for i in range(10000):
    if data[i]!=0:
        for j in range(data[i]):
            print(i+1)



#모든 입력을 배열에 저장하면 메모리 초과이다.
#이 문제에서 메모리 제한은 8MB이다.