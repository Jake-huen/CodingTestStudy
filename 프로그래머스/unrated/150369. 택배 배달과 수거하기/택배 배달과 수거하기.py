def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    have_deliver = 0
    have_pickup = 0
    for i in range(n):
        have_deliver += deliveries[i] # 일단 채워준다
        have_pickup += pickups[i] # 일단 채워준다
        while have_deliver>0 or have_pickup>0:
            have_deliver -= cap
            have_pickup -= cap
            answer+=(n-i)*2
    return answer