def solution(cap, n, deliveries, pickups):
    suffixSumD = [delivery for delivery in deliveries]
    suffixSumP = [pickup for pickup in pickups]

    for idx in range(n - 2, -1, -1):
        suffixSumD[idx] = suffixSumD[idx + 1] + suffixSumD[idx]
        suffixSumP[idx] = suffixSumP[idx + 1] + suffixSumP[idx]

    sumCap = 0
    answer = 0
    for idx in range(n - 1, -1, -1):
        target = max(suffixSumD[idx], suffixSumP[idx])
        if target == 0: break
        if target > sumCap:
            visitFrequency = (target - sumCap) // cap + (1 if target % cap else 0)
            answer += (idx + 1) * visitFrequency
            sumCap += visitFrequency * cap

    return answer * 2


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
