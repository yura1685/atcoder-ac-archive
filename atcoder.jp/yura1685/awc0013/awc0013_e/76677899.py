from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
g = MFGraph(N + M + 2)
for i in range(1, N+1):
    g.add_edge(0, i, 1)
for i in range(N+1, N+M+1):
    g.add_edge(i, N+M+1, 1)

for i in range(1, N+1):
    K, *C = map(int, input().split())
    for j in C:
        g.add_edge(i, j+N, 1)
    
ans = g.flow(0, N+M+1, min(N, M))
print(ans)