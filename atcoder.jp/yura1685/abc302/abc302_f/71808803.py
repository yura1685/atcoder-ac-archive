N, M = map(int,input().split())

# 1~N は集合，N+i は数字
g = [[] for _ in range(N+M+1)]
for i in range(N):
    A = int(input())
    S = list(map(int,input().split()))
    for s in S:
        g[i].append(N+s)
        g[N+s].append(i)

from collections import deque

d = deque([N+1])
inf = float('inf')
step = [inf] * (N+M+1)
step[N+1] = 0

while d:
    u = d.popleft()
    for v in g[u]:
        if step[u] + 1 < step[v]:
            step[v] = step[u] + 1
            d.append(v)

print(step[N+M]//2-1 if step[N+M] < inf else -1)