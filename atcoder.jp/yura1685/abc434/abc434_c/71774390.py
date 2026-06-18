def solve():
    N, H = map(int,input().split())
    points = [tuple(map(int,input().split())) for _ in range(N)]
    Low, High = H, H
    last = 0
    for t, l, u in points:
        diff = t - last
        last = t
        Low = max(Low-diff, 0)
        High = High + diff
        if High < l or Low > u:
            print('No')
            return
        Low = max(Low, l)
        High = min(High, u)
    print('Yes')
    return

for _ in range(int(input())): solve()