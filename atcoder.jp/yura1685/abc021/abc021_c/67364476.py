from collections import deque
from functools import cache

N = int(input())
a, b = map(int,input().split())
M = int(input())
g = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)

check = [0]*(N+1)
check[a] = 1
dis = [float('inf')]*(N+1)
dis[a] = 0
d = deque([a])

while d:
    u = d.popleft()
    for v in g[u]:
        if check[v] == 0:
            check[v] = 1
            dis[v] = dis[u] + 1
            d.append(v)

ans = 1
mod = 10**9 + 7

@cache
def f(u):
    if u == a:
        return 1
    return sum([f(v) for v in g[u] if dis[v] < dis[u]]) % mod

print(f(b))