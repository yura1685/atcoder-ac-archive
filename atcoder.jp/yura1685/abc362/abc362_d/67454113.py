import heapq

N, M = map(int,input().split())
A = list(map(int,input().split()))
g = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int,input().split())
    g[U-1].append((V-1,B))
    g[V-1].append((U-1,B))

W = [A[0]] + [float('inf')]*(N-1)

hq = [(A[0],0)] # 重み，頂点
heapq.heapify(hq)

check = [0]*N

while hq:
    w, u = heapq.heappop(hq) # 頂点 u と、その現在の重さ w
    if check[u]:
        continue
    check[u] = 1
    for v, b in g[u]: # uからvへのパスとその重さb
        if w + b + A[v] < W[v]:
            W[v] = w + b + A[v]
            heapq.heappush(hq,(W[v],v))

print(*W[1:])