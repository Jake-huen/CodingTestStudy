poems = list(input().split())  # 5000을 넘지 않는 문자열
space = int(input())
alp_left = list(map(int, input().split()))
ans = []
for poem in poems:
    for i in range(len(poem)):
        temp = poem[i]
        if i == 0:
            if temp.isupper():  # 대문자인 경우
                alp_left[ord(temp) - ord('A')] -= 2
                if alp_left[ord(temp) - ord('A')] < 0:
                    print(-1)
                    exit(0)
                else:
                    ans.append(temp)
            elif temp.islower():
                alp_left[ord(temp) - ord('a')] -= 2
                if alp_left[ord(temp) - ord('a')] < 0:
                    print(-1)
                    exit(0)
                else:
                    ans.append(temp.upper())
        else:
            if temp != poem[i - 1]:
                if temp.isupper():  # 대문자인 경우
                    alp_left[ord(temp) - ord('A')] -= 1
                    if alp_left[ord(temp) - ord('A')] < 0:
                        print(-1)
                        exit(0)
                elif temp.islower():
                    alp_left[ord(temp) - ord('a')] -= 1
                    if alp_left[ord(temp) - ord('a')] < 0:
                        print(-1)
                        exit(0)
    if poem!=poems[-1]:
        space-=1
    if space < 0:
        print(-1)
        exit(0)
for i in range(len(ans)):
    print(ans[i], end='')
