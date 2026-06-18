import heapq

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

Q, K = map(int,input().split())

dis = [float('inf')]*(N+1)
dis[K] = 0

P = [(0,K)]
heapq.heapify(P)

while P:
    w, u = heapq.heappop(P)
    d = {}
    for v, c in g[u]:
        if w+c < dis[v]:
            dis[v] = w+c
            d[v] = w+c
    for s in d:
        heapq.heappush(P,(d[s],s))

for _ in range(Q):
    x, y = map(int,input().split())
    print(dis[x]+dis[y])