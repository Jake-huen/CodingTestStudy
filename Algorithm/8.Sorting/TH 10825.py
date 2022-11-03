# 국어 점수 감소 순
# 국어 점수 같으면 영어 점수 증가 순
# 국어 점수, 영어 점수 같으면 수학 점수 감소 순
# 모든 점수 같으면 이름이 사전 순으로 증가하는 순
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))
arr.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in range(n):
    print(arr[i][0])
