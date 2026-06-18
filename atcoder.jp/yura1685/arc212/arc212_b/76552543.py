import heapq

N, M = map(int, input().split())
x1, y1, c1 = map(int, input().split())
x1, y1 = x1-1, y1-1
g = [[] for _ in range(N)]
for _ in range(M-1):
    x, y, c = map(int, input().split())
    g[x-1].append((y-1, c))

inf = 10 ** 18
dist = [inf] * N
dist[y1] = 0
hq = [(0, y1)]
heapq.heapify(hq)
while hq:
    d, u = heapq.heappop(hq)
    if dist[u] < d:
        continue
    for v, w in g[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            heapq.heappush(hq, (d + w, v))

print(c1 + dist[x1] if dist[x1] < inf else -1)