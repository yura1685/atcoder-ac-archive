from collections import defaultdict

dx, dy = defaultdict(set), defaultdict(set)

N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    dx[x].add(y)

ans = 0
for x1 in dx:
    for x2 in dx:
        if x1 >= x2:
            continue
        y = dx[x1] & dx[x2]
        n = len(y)
        ans += n*(n-1)//2

print(ans)