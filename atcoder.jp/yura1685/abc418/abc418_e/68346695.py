from collections import defaultdict
from math import gcd

INF = float('INF')
N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]
d = defaultdict(int)
dc = defaultdict(int)

for i in range(N-1):
    for j in range(i+1,N):
        x1, y1 = P[i]
        x2, y2 = P[j]
        dc[(x1+x2,y1+y2)] += 1
        dx, dy = x2-x1, y2-y1
        if dx < 0:
            dx, dy = -dx, -dy
        g = gcd(dx,dy)
        dx, dy = dx//g, dy//g
        if dx == 0:
            dy = 1
        if dy == 0:
            dx = 1
        a = (dx, dy)
        d[a] += 1


ans = 0
for i in d.values():
    ans += i*(i-1)//2

for i in dc.values():
    ans -= i*(i-1)//2

print(ans)