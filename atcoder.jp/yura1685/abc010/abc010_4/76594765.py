from atcoder.maxflow import MFGraph

N, M, E = map(int, input().split())
G = MFGraph(N+1)
P = list(map(int, input().split()))
for p in P:
    G.add_edge(p, N, 1)
    G.add_edge(N, p, 1)
for _ in range(E):
    a, b = map(int, input().split())
    G.add_edge(a, b, 1)
    G.add_edge(b, a, 1)
print(G.flow(0, N))