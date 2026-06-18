from atcoder.maxflow import MFGraph

N, M = map(int,input().split())
g = MFGraph(N)
for _ in range(M):
    A, B, C = map(int,input().split())
    g.add_edge(A-1, B-1, C)

print(g.flow(0, N-1))