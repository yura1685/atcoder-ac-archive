from collections import defaultdict
import heapq

N, M = map(int,input().split())
H = [int(h) for h in input().split()]
g = defaultdict(list)

for _ in range(M):
    u, v = map(int,input().split())
    u, v = u-1, v-1
    if H[u] >= H[v]:
        g[u].append((v,0))
        g[v].append((u,H[u]-H[v]))
    else:
        g[u].append((v,H[v]-H[u]))
        g[v].append((u,0))

P = [(0,0)]
heapq.heapify(P)

d = [float('inf')]*N
d[0] = 0

while P:
    cur_cost, u = heapq.heappop(P)
    if cur_cost > d[u]:
        continue
    for v, cost in g[u]:
        if d[u] + cost < d[v]:
            d[v] = d[u] + cost
            heapq.heappush(P,(d[v], v))

ans = 0
for i in range(N):
    if d[i] == float('inf'):
        continue
    score = (H[0] - H[i]) - d[i]
    ans = max(ans, score)

print(ans)