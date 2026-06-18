import heapq, math

N = int(input())
P = []
for _ in range(N):
    I = input().split()
    x, y, t, r = int(I[0]), int(I[1]), int(I[2]), int(I[3])
    P.append((x, y, t, r))

inf = 1e18
G = [[inf] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            G[i][j] = 0.0
            continue
        s = min(P[i][2], P[j][3])
        dx, dy = P[j][0] - P[i][0], P[j][1] - P[i][1]
        G[i][j] = math.hypot(dx, dy) / s

Dist = [inf] * N
Dist[0] = 0.0

hq = [(0.0, 0)]
while hq:
    d, u = heapq.heappop(hq)
    if Dist[u] < d: continue
    for v in range(N):
        if Dist[u] + G[u][v] < Dist[v]:
            Dist[v] = Dist[u] + G[u][v]
            heapq.heappush(hq, (Dist[v], v))

L = sorted(Dist, reverse=True)
for i in range(N-1):
    L[i] += i

print(f"{max(L):.10f}")