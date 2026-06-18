from math import isqrt
from heapq import *

def f(C, D, t):
    n = max(t+1, isqrt(D))
    return C - 1 + min(n + D // n, (n+1) + D // (n+1))

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C, D = map(int, input().split())
    A, B = A-1, B-1
    g[A].append((B, C, D))
    g[B].append((A, C, D))

hq = []
heappush(hq, (0, 0))
inf = 10 ** 18
time = [0] + [inf] * (N-1)

while hq:
    t, u = heappop(hq)
    if time[u] < t:
        continue
    for v, c, d in g[u]:
        t2 = f(c, d, t)
        if t2 < time[v]:
            time[v] = t2
            heappush(hq, (t2, v))

print(time[-1] if time[-1] < inf else -1)