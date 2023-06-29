def trap(height):
    ans = 0
    check = max(height)
    max_idx = []
    for i in range(len(height)):
        if height[i] == check:
            max_idx.append(i)
    left = []
    right = []
    mid = []
    for i in range(len(height)):
        if i < max_idx[0]:
            left.append(i)
        elif i > max_idx[-1]:
            right.append(i)
        else:
            mid.append(i)
    if len(left) > 0:
        check = left[0]
        for i in range(1, len(left)):
            if left[i] < check:
                ans += check - left[i]
            elif left[i] > check:
                check = left[i]
    if len(right) > 0:
        check = right[-1]
        for i in range(len(right) - 1, -1, -1):
            if right[i] < check:
                ans += check - right[i]
            elif right[i] > check:
                check = right[i]
    if len(mid) > 0:
        check = max(mid)
        for i in range(len(mid)):
            ans += check - mid[i]
    return ans


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# trap([1, 1, 1, 1, 1, 1])
