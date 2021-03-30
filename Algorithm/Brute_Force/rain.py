def trapping_rain(buildings):
    # 코드를 작성하세요
    big= buildings[0]
    r_max = max(buildings)
    result = 0
    for i in range(len(buildings)-1):
        if buildings[i]<=big:
            result+=big-buildings[i]
        else:
            if buildings[i]!=r_max:
                big=buildings[i]
            else:continue
    return result

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))