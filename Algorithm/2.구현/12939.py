def solution(s):
    temp = list(map(int,s.split()))
    answer = ''
    answer+=str(min(temp))
    answer+=' '
    answer+=str(max(temp))
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))