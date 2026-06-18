N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))

inf = float('inf')
path = [inf] * N
path[0] = 0

import heapq

hq = [(0,0)] # (距離，頂点)
heapq.heapify(hq)

while hq:
    w, u = heapq.heappop(hq)
    if w > path[u]: continue
    for v, w2 in g[u]:
        if w + w2 < path[v]:
            heapq.heappush(hq, (w+w2, v))
            path[v] = w + w2

for i in range(N):
    print(-1 if path[i] == inf else path[i])