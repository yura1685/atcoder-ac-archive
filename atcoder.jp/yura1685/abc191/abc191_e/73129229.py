from heapq import heappop, heappush

N, M = map(int,input().split())
g = [[] for _ in range(N)]
revg = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int,input().split())
    g[A-1].append((B-1,C))
    revg[B-1].append((A-1,C))

inf = float('inf')
d = [[inf]*N for _ in range(N)]

for i in range(N):
    hq = []
    heappush(hq,(0,i))
    while hq:
        w, u = heappop(hq)
        for v, cost in g[u]:
            if w + cost < d[i][v]:
                d[i][v] = w + cost
                heappush(hq, (d[i][v], v))

ans = [d[i][i] for i in range(N)]
for u in range(N):
    for v in range(N):
        ans[u] = min(ans[u], d[u][v] + d[v][u])

for a in ans:
    print(a if a < inf else -1)