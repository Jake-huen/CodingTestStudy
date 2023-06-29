def trap(height):
    ans = 0
    for i in range(1, len(height) - 1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        check = min(left_max, right_max)
        if height[i] < check:
            ans += check - height[i]
    print(ans)


# trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
trap([1, 1, 1, 1, 1, 1])
