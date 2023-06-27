def solution(n, words):
    round = 0
    end_word = words[0][0]
    while True:
        for i in range(n):
            if round * n + i > len(words) - 1:
                return [0, 0]
            elif words[round * n + i] in words[:round * n + i]:  # 중복
                # print("중복")
                return [round + 1, i + 1]
            elif words[round * n + i][0] != end_word:
                # print("글자 다름")
                return [round + 1, i + 1]
            else:
                end_word = words[round * n + i][-1]
                # print(end_word)
        round += 1


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
