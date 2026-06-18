import heapq

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
edge = [list(map(int,input().split())) for _ in range(M)]
for a, b, c in edge:
    g[a].append((b,c))
    g[b].append((a,c))

ans = 0
for a, b, c in edge:
    dis = [float('inf')]*(N+1)
    dis[a] = 0
    P = [(0,a)]
    heapq.heapify(P)
    while True:
        w, u = heapq.heappop(P)
        if u == b:
            W = w
            break
        d = {}
        for v, x in g[u]:
            if w + x < dis[v]:
                dis[v] = w+x
                d[v] = w+x
        for s in d:
            heapq.heappush(P,(d[s],s))
    if W < c:
        ans += 1

print(ans)