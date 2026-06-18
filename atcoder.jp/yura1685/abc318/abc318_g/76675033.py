from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
G = MFGraph(2*N+1)
A, B, C = map(int, input().split())
G.add_edge(A + N, 0, 1)
G.add_edge(C + N, 0, 1)
for i in range(1, N+1):
    G.add_edge(i, i + N, 1)
for _ in range(M):
    U, V = map(int, input().split())
    G.add_edge(U + N, V, 1)
    G.add_edge(V + N, U, 1)
ans = G.flow(B + N, 0, 2)
print('Yes' if ans > 1 else 'No')