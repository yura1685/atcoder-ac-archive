from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
g = MFGraph(N + M + 2)
B = list(map(int, input().split()))
for i, b in enumerate(B):
    g.add_edge(0, i + 1, b)
for i in range(M+1, N+M+1):
    K, *C = map(int, input().split())
    for j in C:
        g.add_edge(j, i, 1)
    g.add_edge(i, N+M+1, 1)
print(g.flow(0, N+M+1,min(sum(B), N)))