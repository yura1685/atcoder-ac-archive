import heapq

N = int(input())

g = [[] for _ in range(N+1)]
for i in range(1,N):
    A, B, X = map(int,input().split())
    if X == i+1:
        g[i].append((X,min(A,B)))
        continue
    g[i].append((i+1,A))
    g[i].append((X,  B))

d = [float('inf')]*(N+1)
d[1] = 0

P = [(0,1)]
heapq.heapify(P)
while P:
    w, u = heapq.heappop(P)
    for v, t in g[u]:
        if w + t < d[v]:
            d[v] = w+t
            heapq.heappush(P,(w+t,v))

print(d[N])