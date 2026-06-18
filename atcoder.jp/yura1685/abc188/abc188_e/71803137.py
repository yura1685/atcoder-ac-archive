N, M = map(int,input().split())
A = list(map(int,input().split()))
g = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(int,input().split())
    g[X-1].append(Y-1)
inf = float('inf')
B = [inf] * N
for u in range(N):
    for v in g[u]:
        B[v] = min(B[v], B[u], A[u])

print(max(A[i]-B[i] for i in range(N)))