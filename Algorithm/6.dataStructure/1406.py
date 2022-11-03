from sys import stdin
input = stdin.readline
first = list(stdin.readline().strip())
second = []
m= int(input())
for i in range(m):
    question=input().split()
    if question[0]=='L':
        if first: #첫번째 스택이 존재할때 (없으면 더 왼쪽으로 커서가 못가니까)
            second.append(first.pop())
    elif question[0]=='D':
        if second:
            first.append(second.pop())
    elif question[0]=='B':
        if first:
            first.pop()
    elif question[0]=='P':
        first.append(question[1])
print("".join(first+list(reversed(second))))
