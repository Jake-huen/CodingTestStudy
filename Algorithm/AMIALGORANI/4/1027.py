"""
i번째 빌딩 (i,0) ~ (i,높이)
"""

n = int(input())
buildings = list(map(int, input().split()))


def giulgi(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


for idx, build in enumerate(buildings):
    right = min(len(buildings), idx + 1)
    left = max(0, idx - 1)
    for i in range(right, n + 1):
        slope = giulgi(build)
