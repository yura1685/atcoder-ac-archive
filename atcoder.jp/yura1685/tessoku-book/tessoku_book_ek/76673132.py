import heapq

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    g[A-1].append((B-1, C))
    g[B-1].append((A-1, C))

inf = 10 ** 18
From = [-1] * N
Dist = [inf] * N
Dist[0] = 0
hq = []
heapq.heappush(hq, (0, 0))

while hq:
    d, u = heapq.heappop(hq)
    if Dist[u] < d:
        continue
    for v, w in g[u]:
        if Dist[u] + w < Dist[v]:
            Dist[v] = Dist[u] + w
            heapq.heappush(hq, (Dist[v], v))
            From[v] = u

now = N-1
ans = []
while now != -1:
    ans.append(now + 1)
    now = From[now]
ans.reverse()
print(*ans)