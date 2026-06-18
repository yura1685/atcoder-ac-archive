import heapq

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(1, M+1):
    A, B, C = map(int, input().split())
    A, B = A-1, B-1
    g[A].append((B, i, C))
    g[B].append((A, i, C))

inf = float('inf')
dist = [inf] * N
dist[0] = 0
frm = [-1] * N

hq = []
heapq.heappush(hq, (0, 0, -1))
while hq:
    d, u, e = heapq.heappop(hq)
    if dist[u] < d:
        continue
    if e != -1:
        frm[u] = e
    for v, i, w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(hq, (dist[v], v, i))

print(*frm[1:])