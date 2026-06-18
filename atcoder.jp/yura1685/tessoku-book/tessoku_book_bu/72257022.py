from heapq import heapify, heappop, heappush

N, M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int,input().split())
    g[a-1].append((b-1,c,d))
    g[b-1].append((a-1,c,d))

hq = [(0,0,0)] # (距離，-木, 頂点)
heapify(hq)
Min = [(float('inf'), 0) for _ in range(N)]
Min[0] = (0,0)

while hq:
    d, t, u = heappop(hq)
    for v, c, ki in g[u]:
        if (d+c, t-ki) < Min[v]:
            heappush(hq, (d+c, t-ki, v))
            Min[v] = (d+c, t-ki)

print(Min[-1][0], -Min[-1][1])